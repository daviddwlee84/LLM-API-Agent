from langchain_community.agent_toolkits.openapi.spec import (
    reduce_openapi_spec,
    ReducedOpenAPISpec,
)
import tiktoken
import requests
import yaml
from urllib.parse import urlparse
import os


class OpenAPIManager:
    """
    https://python.langchain.com/docs/integrations/toolkits/openapi

    TODO:
    1. (automatically) set auth header
    2. RequestWrapper
    3. Get Agent
    """

    _spec: ReducedOpenAPISpec
    _raw_spec: dict | list
    _spec_path: str

    def __init__(
        self, yaml_url_or_path: str | None = None, default_model: str = "gpt-4"
    ):
        self.encoder = tiktoken.encoding_for_model(default_model)
        self._spec_path = yaml_url_or_path

        if yaml_url_or_path is not None:
            if self.is_local(yaml_url_or_path):
                self._spec = self.load_local_yaml(yaml_url_or_path)
            else:
                self._spec = self.load_online_yaml(yaml_url_or_path)

    @staticmethod
    def is_local(url_or_path: str) -> bool:
        """
        https://stackoverflow.com/questions/68626097/pythonic-way-to-identify-a-local-file-or-a-url
        """
        url_parsed = urlparse(url_or_path)
        if url_parsed.scheme in ("file", ""):  # Possibly a local file
            return os.exists(url_parsed.path)
        return False

    @property
    def spec_tokens(self):
        def count_tokens(string: str):
            """
            *** ValueError: Encountered text corresponding to disallowed special token '<|endoftext|>'.
            https://github.com/langchain-ai/langchain/issues/923
            https://github.com/langchain-ai/langchain/pull/924
            """
            # return len(self.encoder.encode(string, disallowed_special=()))
            return len(self.encoder.encode(string))

        return count_tokens(yaml.dump(self._spec))

    @property
    def spec_endpoints(self) -> int:
        return len(self._spec.endpoints)

    @property
    def raw_spec_endpoints(self) -> int:
        endpoints = [
            (route, operation)
            for route, operations in self._raw_spec["paths"].items()
            for operation in operations
            if operation in ["get", "post"]
        ]
        return len(endpoints)

    def load_online_yaml(
        self, yaml_url: str, update_spec: bool = True
    ) -> ReducedOpenAPISpec:
        """
        https://stackoverflow.com/questions/65191010/how-to-load-a-yaml-file-from-url-to-process-in-python
        """
        response = requests.get(yaml_url, allow_redirects=True)
        raw_api_spec = yaml.safe_load(response.content.decode("utf-8"))
        api_spec = reduce_openapi_spec(raw_api_spec)

        if update_spec:
            self._spec = api_spec
            self._spec_path = yaml_url
            self._raw_spec = raw_api_spec
        return api_spec

    def load_local_yaml(
        self, yaml_path: str, update_spec: bool = True
    ) -> ReducedOpenAPISpec:
        with open(yaml_path) as f:
            raw_api_spec = yaml.load(f, Loader=yaml.Loader)
        api_spec = reduce_openapi_spec(raw_api_spec)

        if update_spec:
            self._spec = api_spec
            self._spec_path = yaml_path
            self._raw_spec = raw_api_spec
        return api_spec


if __name__ == "__main__":
    manager = OpenAPIManager(
        "https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/spotify.com/1.0.0/openapi.yaml"
    )
    print(manager._spec)
    print(type(manager._spec))
    print(type(manager._raw_spec))
    print(manager.spec_tokens)
    print(manager.spec_endpoints)
    print(manager.raw_spec_endpoints)
    # import ipdb; ipdb.set_trace()
    # manager2 = OpenAPIManager(reduce_spec=False)
    # manager2.load_online_yaml("https://raw.githubusercontent.com/openai/openai-openapi/master/openapi.yaml")
    # print(manager2._spec)
    # print(type(manager2._spec))
    # print(manager2.spec_tokens)
    # print(manager2.spec_endpoints)
    # import ipdb; ipdb.set_trace()

    import spotipy.util as util
    from langchain.requests import RequestsWrapper

    from dotenv import load_dotenv

    curr_dir = os.path.dirname(os.path.abspath(__file__))

    load_dotenv(os.path.join(curr_dir, "../.env"))

    def construct_spotify_auth_headers(raw_spec: dict):
        scopes = list(
            raw_spec["components"]["securitySchemes"]["oauth_2_0"]["flows"][
                "authorizationCode"
            ]["scopes"].keys()
        )
        access_token = util.prompt_for_user_token(scope=",".join(scopes))
        return {"Authorization": f"Bearer {access_token}"}

    # Get API credentials.
    headers = construct_spotify_auth_headers(manager._raw_spec)
    print(headers)
    requests_wrapper = RequestsWrapper(headers=headers)
    print(requests_wrapper)

    from langchain_community.agent_toolkits.openapi import planner
    from langchain_openai import AzureChatOpenAI

    llm = AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        openai_api_version=os.getenv("OPENAI_API_VERSION"),
    )
    print(llm)

    from langchain.agents.agent import AgentExecutor

    # ValueError: You must set allow_dangerous_requests to True to use this tool. Request scan be dangerous and can lead to security vulnerabilities. For example, users can ask a server to make a request to an internalserver. It's recommended to use requests through a proxy server and avoid accepting inputs from untrusted sources without proper sandboxing.Please see: https://python.langchain.com/docs/security for further security information.
    # https://github.com/langchain-ai/langchain/issues/19440
    # https://api.python.langchain.com/en/latest/agent_toolkits/langchain_community.agent_toolkits.openapi.toolkit.RequestsToolkit.html
    spotify_agent: AgentExecutor = planner.create_openapi_agent(
        manager._spec,
        requests_wrapper,
        llm,
        # https://github.com/langchain-ai/langchain/pull/19493
        allow_dangerous_requests=True,
    )
    spotify_agent
    print(spotify_agent)
    print(len(spotify_agent.tools))

    import ipdb

    ipdb.set_trace()
    user_query = "give me a song I'd like, make it blues-ey (answer shortly)"
    # openai.BadRequestError: Error code: 400 - {'error': {'message': "This model's maximum context length is 16384 tokens. However, your messages resulted in 27000 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}
    response = spotify_agent.invoke(user_query)
    print(response)

    import ipdb

    ipdb.set_trace()
