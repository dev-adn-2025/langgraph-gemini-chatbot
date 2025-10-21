from langchain_tavily import TavilySearch

def search_web(query_search: str) -> str:
    """ Retrieve docs from web search """
    tavily_search = TavilySearch(max_results=2)
    search_docs = tavily_search.invoke(query_search)

    results = search_docs.get("results", [])

    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document href="{doc["url"]}" title="{doc["title"]}">\n{doc["content"]}\n</Document>'
            for doc in results
        ]
    )

    return formatted_search_docs