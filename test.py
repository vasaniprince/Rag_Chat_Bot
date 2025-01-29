import requests
import json

def test_rag_system():
    BASE_URL = 'http://localhost:5000'
    
    # 1. First add some knowledge
    knowledge_data = {
        "text": """
        Cricket in India has a rich history dating back to 1721. The first cricket club was established 
        in Calcutta in 1792. India played its first Test match in 1932 against England at Lord's. 
        The Board of Control for Cricket in India (BCCI) was formed in 1928. India won its first 
        Test series against England in 1952. The country's biggest cricket achievement came in 1983 
        when India won the World Cup under Kapil Dev's leadership. India won its second World Cup 
        in 2011 under MS Dhoni's captaincy. The Indian Premier League (IPL) was started in 2008 
        and has become one of the world's most valuable cricket leagues.
        """
    }
    
    # Add knowledge
    print("\nAdding knowledge...")
    add_response = requests.post(
        f"{BASE_URL}/add_knowledge",
        json=knowledge_data,
        headers={"Content-Type": "application/json"}
    )
    print("Add Knowledge Response:", add_response.json())
    
    # 2. Then test with a query
    query_data = {
        "query": "When did India win its first World Cup?",
        "context": "cricket history"
    }
    
    print("\nQuerying the system...")
    chat_response = requests.post(
        f"{BASE_URL}/chat",
        json=query_data,
        headers={"Content-Type": "application/json"}
    )
    print("Chat Response:", chat_response.json())

if __name__ == "__main__":
    test_rag_system()