from serpapi import GoogleSearch
 
class DuckDuckSearch:
    def __init__(self, api_key):
        """
        Init new instance for Duck Duck Go
 
        Args:
        api_key (str): Duck Duck go
        """
        self.api_key = api_key
 
    def search(self, query, lang="es-es"):
        params = {
          "engine": "duckduckgo",
          "q": query,
          "kl": lang,
          "api_key": self.api_key
        }
 
        final_results = []
        search = GoogleSearch(params)
        results = search.get_dict()
        
        if (results["search_metadata"]["status"] == "Success" ):
            organicResults = results["organic_results"]
            cresults = self.custom_results(organicResults)
            final_results.extend(cresults)
        else:
            print("Error getting search results")
        return final_results
 
    def custom_results(self, results):
        """Filter results"""
        custom_results = []
        for res in results:
            cresult = {}
            cresult["title"] = res.get("title")
            cresult["snippet"] = res.get("snippet")
            cresult["link"] = res.get("link")
            custom_results.append(cresult)
        return custom_results






