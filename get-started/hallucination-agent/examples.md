---
title: Hallucination Detection Examples
description: Explore practical examples of how to use kluster.ai's hallucination detection service to identify and prevent AI hallucinations in various application scenarios.
---

# Hallucination Detection Examples

This page provides practical examples of using kluster.ai's hallucination detection service in different scenarios. Examples demonstrate both question-answer validation and chat completion validation to help you understand how hallucination detection can be implemented in your applications.

## Basic example

This example shows a simple hallucination check comparing an AI response against a short context:

```python
import requests
import json

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.kluster.ai/v1/judges/detect-hallucination"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Example 1: Factual response
data = {
    "prompt": "When was the Berlin Wall demolished?",
    "output": "The Berlin Wall began to be demolished in 1989.",
    "context": "The Berlin Wall stood from 1961 to 1989, when it was opened on November 9, 1989. Demolition officially began in 1990 and was completed in 1992.",
    "return_search_results": False
}

response = requests.post(API_URL, headers=headers, data=json.dumps(data))
print(json.dumps(response.json(), indent=2))

# Example 2: Hallucinated response
data = {
    "prompt": "When was the Berlin Wall demolished?",
    "output": "The Berlin Wall was demolished in 1995 after extensive planning by the European Union.",
    "context": "The Berlin Wall stood from 1961 to 1989, when it was opened on November 9, 1989. Demolition officially began in 1990 and was completed in 1992.",
    "return_search_results": False
}

response = requests.post(API_URL, headers=headers, data=json.dumps(data))
print(json.dumps(response.json(), indent=2))
```

## Chat Completion Examples

The following examples demonstrate how to use the Chat Completion format for hallucination detection.

```python
import requests
import json

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.kluster.ai/v1/judges/detect-hallucination"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Example: Scientific claim verification
data = {
    "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are a scientific expert that provides accurate information based on peer-reviewed research."
        },
        {
            "role": "user",
            "content": "Is there any scientific evidence that coffee is beneficial for health?"
        },
        {
            "role": "assistant",
            "content": "Yes, multiple studies have shown that coffee consumption is associated with lower risk of several diseases including type 2 diabetes, Parkinson's disease, and certain liver conditions. The antioxidants in coffee appear to be responsible for many of these benefits."
        }
    ],
    "max_tokens": 3600,
    "temperature": 0.6,
    "top_p": 0.5,
    "stream": False
}

response = requests.post(API_URL, headers=headers, data=json.dumps(data))
print(json.dumps(response.json(), indent=2))

# Example: Hallucinated medical claim
data = {
    "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are a medical advisor providing evidence-based health information."
        },
        {
            "role": "user",
            "content": "Can vitamin supplements prevent cancer?"
        },
        {
            "role": "assistant",
            "content": "Yes, taking high doses of vitamin C, E, and selenium has been conclusively proven to prevent most types of cancer in multiple large-scale clinical trials."
        }
    ],
    "max_tokens": 3600,
    "temperature": 0.6,
    "top_p": 0.5,
    "stream": False
}

response = requests.post(API_URL, headers=headers, data=json.dumps(data))
print(json.dumps(response.json(), indent=2))
```

### Example: Customer Support Quality Assurance

This example shows how to implement hallucination detection in a customer support workflow:

```python
import requests
import json

def verify_customer_support_response(conversation_history):
    """
    Verify if a customer support agent's response contains hallucinated information.
    
    Args:
        conversation_history: List of message objects representing the conversation.
        
    Returns:
        Tuple of (is_acceptable, explanation)
    """
    API_KEY = "YOUR_API_KEY"
    API_URL = "https://api.kluster.ai/v1/judges/detect-hallucination"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": "klusterai/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": conversation_history,
        "max_tokens": 3600,
        "temperature": 0.6,
        "top_p": 0.5,
        "stream": False
    }
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        result = response.json()
        
        if result["is_hallucination"]:
            return (False, f"Response contains inaccurate information: {result['explanation']}")
        else:
            return (True, "Response verified as accurate")
    except Exception as e:
        return (False, f"Verification error: {str(e)}")

# Example usage
conversation = [
    {
        "role": "system",
        "content": "You are a customer support agent for TechPro, a company that sells laptops, smartphones, and tablets. Provide accurate information about our products and policies."
    },
    {
        "role": "user",
        "content": "What's your refund policy for laptops?"
    },
    {
        "role": "assistant",
        "content": "All TechPro laptops come with a 90-day no-questions-asked refund guarantee. After 90 days, you can still return your laptop for a full refund if it develops any hardware issues within the 3-year warranty period."
    }
]

is_acceptable, explanation = verify_customer_support_response(conversation)

if is_acceptable:
    print("✅ Response approved for customer delivery")
else:
    print(f"⚠️ Response flagged for review: {explanation}")
```

## Real-world scenarios

### Scenario 1: Educational content verification

In this example, we're building an educational application that validates AI-generated historical content:

```python
import requests
import json

def verify_historical_content(topic, ai_generated_content, historical_sources):
    """
    Verify AI-generated historical content against trusted sources.
    
    Args:
        topic: The historical topic being discussed
        ai_generated_content: The AI-generated explanation or narrative
        historical_sources: Text from trusted historical references
        
    Returns:
        Dictionary with verification results
    """
    API_KEY = "YOUR_API_KEY"
    API_URL = "https://api.kluster.ai/v1/judges/detect-hallucination"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "prompt": f"Provide information about {topic}",
        "output": ai_generated_content,
        "context": historical_sources,
        "return_search_results": True
    }
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        result = response.json()
        
        if result["is_hallucination]:
            return {
                "verified": False,
                "explanation": result["explanation"],
                "action_needed": "Content requires factual corrections"
            }
        else:
            return {
                "verified": True,
                "explanation": result["explanation"],
                "action_needed": None
            }
    except Exception as e:
        return {
            "verified": False,
            "explanation": f"Error during verification: {str(e)}",
            "action_needed": "Verification service unavailable, manual review required"
        }

# Example usage
historical_topic = "The Apollo 11 moon landing"
ai_content = """
The Apollo 11 mission successfully landed humans on the moon on July 20, 1969.
Neil Armstrong and Buzz Aldrin walked on the lunar surface while Michael Collins
orbited in the command module. Armstrong's first words upon stepping on the moon were
'That's one small step for man, one giant leap for mankind.'
"""
historical_source = """
Apollo 11 was the spaceflight that first landed humans on the Moon. Commander Neil Armstrong
and lunar module pilot Buzz Aldrin formed the American crew that landed the Apollo Lunar
Module Eagle on July 20, 1969, at 20:17 UTC. Armstrong became the first person to step 
onto the lunar surface six hours and 39 minutes later on July 21 at 02:56 UTC; Aldrin 
joined him 19 minutes later. They spent about two and a quarter hours together outside 
the spacecraft, and they collected 47.5 pounds (21.5 kg) of lunar material to bring back 
to Earth. Command module pilot Michael Collins flew the Command Module Columbia alone in 
lunar orbit while they were on the Moon's surface.
"""

verification_result = verify_historical_content(historical_topic, ai_content, historical_source)
print(json.dumps(verification_result, indent=2))
```

### Scenario 2: Medical information verification

In this example, we're building a healthcare application that verifies AI-generated medical information:

```python
def verify_medical_information(medical_query, ai_response, medical_literature):
    """
    Verify AI-generated medical information against peer-reviewed literature.
    
    Args:
        medical_query: The medical question asked
        ai_response: The AI-generated medical information
        medical_literature: Text from peer-reviewed medical sources
        
    Returns:
        Dictionary with verification results and safety recommendations
    """
    API_KEY = "YOUR_API_KEY"
    API_URL = "https://api.kluster.ai/v1/judges/detect-hallucination"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "prompt": medical_query,
        "output": ai_response,
        "context": medical_literature,
        "return_search_results": True
    }
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        result = response.json()
        
        safety_disclaimer = """
        NOTE: This verification is for informational purposes only and does not constitute
        medical advice. Always consult with a qualified healthcare professional for 
        medical diagnosis, treatment, or advice.
        """
        
        if result["is_hallucination"]:
            return {
                "verified": False,
                "explanation": result["explanation"],
                "safety_recommendation": "Information contains inaccuracies and should NOT be used for medical decisions.",
                "disclaimer": safety_disclaimer
            }
        else:
            return {
                "verified": True,
                "explanation": result["explanation"],
                "safety_recommendation": "Information appears consistent with provided medical literature.",
                "disclaimer": safety_disclaimer
            }
            return {
                "verified": True,
                "explanation": result["explanation"],
                "safety_recommendation": "Information appears consistent with provided medical literature.",
                "disclaimer": safety_disclaimer
            }
    except Exception as e:
        return {
            "verified": False,
            "explanation": f"Error during verification: {str(e)}",
            "safety_recommendation": "Verification failed. Do not use for medical decisions.",
            "disclaimer": safety_disclaimer
        }
```

### Scenario 3: Legal document analysis

This example shows how to validate AI-generated legal analysis against legal texts:

```python
def verify_legal_analysis(legal_question, ai_analysis, legal_texts):
    """
    Verify AI-generated legal analysis against authoritative legal texts.
    
    Args:
        legal_question: The legal question asked
        ai_analysis: The AI-generated legal analysis
        legal_texts: Relevant legal codes, precedents, or authoritative sources
        
    Returns:
        Dictionary with verification results and confidence level
    """
    API_KEY = "YOUR_API_KEY"
    API_URL = "https://api.kluster.ai/v1/judges/detect-hallucination"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "prompt": legal_question,
        "output": ai_analysis,
        "context": legal_texts,
        "return_search_results": True
    }
    
    legal_disclaimer = """
    DISCLAIMER: This verification is not legal advice. The information provided is for
    general informational purposes only and should not be relied upon as legal advice.
    Consult with a qualified attorney for legal advice regarding your specific situation.
    """
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        result = response.json()
        
        if result["is_hallucination"]:
            return {
                "verified": False,
                "confidence": "Low",
                "explanation": result["explanation"],
                "recommendation": "Legal analysis contains statements not supported by provided legal texts.",
                "disclaimer": legal_disclaimer
            }
        else:
            return {
                "verified": True,
                "confidence": "Moderate",
                "explanation": result["explanation"],
                "recommendation": "Legal analysis appears consistent with provided legal texts.",
                "disclaimer": legal_disclaimer
            }
    except Exception as e:
        return {
            "verified": False,
            "confidence": "None",
            "explanation": f"Error during verification: {str(e)}",
            "recommendation": "Verification failed. Manual review required.",
            "disclaimer": legal_disclaimer
        }
```

## Case study: News fact-checking system

Here's a more comprehensive example of implementing a news fact-checking system using the Hallucination Agent:

```python
import requests
import json
import time
from datetime import datetime

class NewsFactChecker:
    """A system to verify facts in news articles against trusted sources."""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.kluster.ai/v1/judges/detect-hallucination"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        self.verification_log = []
    
    def verify_article_against_sources(self, article_text, trusted_sources, article_metadata=None):
        """
        Verify statements in a news article against trusted sources.
        
        Args:
            article_text: The text of the news article to verify
            trusted_sources: Text from verified, trusted sources
            article_metadata: Dictionary with article metadata (title, date, source, etc.)
            
        Returns:
            Dictionary with verification results and detailed analysis
        """
        if article_metadata is None:
            article_metadata = {
                "title": "Unknown",
                "source": "Unknown",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        
        data = {
            "prompt": f"Verify the factual accuracy of this news article: {article_metadata.get('title', 'Unknown')}",
            "output": article_text,
            "context": trusted_sources,
            "return_search_results": True
        }
        
        try:
            start_time = time.time()
            response = requests.post(self.api_url, headers=self.headers, data=json.dumps(data))
            response_time = time.time() - start_time
            
            result = response.json()
            
            # Log verification attempt
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "article_metadata": article_metadata,
                "verification_result": result["is_hallucination"],
                "response_time_seconds": round(response_time, 2),
                "token_usage": result.get("usage", {})
            }
            self.verification_log.append(log_entry)
            
            # Prepare detailed analysis
            if result["is_hallucination"]:
                fact_check_result = {
                    "verified": False,
                    "credibility_score": self._calculate_credibility_score(result, article_metadata),
                    "issues_identified": self._extract_issues(result["explanation"]),
                    "detailed_explanation": result["explanation"],
                    "recommendation": "This article contains information not supported by trusted sources."
                }
            else:
                fact_check_result = {
                    "verified": True,
                    "credibility_score": self._calculate_credibility_score(result, article_metadata),
                    "issues_identified": [],
                    "detailed_explanation": result["explanation"],
                    "recommendation": "This article appears factually consistent with trusted sources."
                }
            
            return fact_check_result
            
        except Exception as e:
            return {
                "verified": False,
                "credibility_score": 0,
                "issues_identified": [f"Verification error: {str(e)}"],
                "detailed_explanation": f"An error occurred during verification: {str(e)}",
                "recommendation": "Verification failed. Manual review required."
            }
    
    def _calculate_credibility_score(self, result, metadata):
        """Calculate a credibility score based on verification result and metadata."""
        base_score = 0 if result["is_hallucination"] else 80
        
        # Adjust score based on source reputation (simplified example)
        trusted_sources = ["Reuters", "Associated Press", "BBC", "The New York Times"]
        if metadata.get("source") in trusted_sources:
            base_score += 10
        
        # Additional scoring criteria could be implemented here
        
        return min(base_score, 100)  # Cap at 100
    
    def _extract_issues(self, explanation):
        """Extract specific issues from the explanation."""
        # This is a simplified example - in production, more sophisticated 
        # NLP techniques could be used to extract specific issues
        lines = explanation.split("\n")
        issues = [line for line in lines if line.strip() and not line.startswith("The")]
        return issues
        
    def get_verification_statistics(self):
        """Get statistics about verifications performed."""
        if not self.verification_log:
            return {"error": "No verifications performed yet"}
            
        total = len(self.verification_log)
        hallucinations_detected = sum(1 for log in self.verification_log if log["verification_result"])
        
        avg_response_time = sum(log["response_time_seconds"] for log in self.verification_log) / total
        
        # Calculate total token usage
        total_tokens = 0
        for log in self.verification_log:
            if "token_usage" in log and "total_tokens" in log["token_usage"]:
                total_tokens += log["token_usage"]["total_tokens"]
        
        return {
            "total_verifications": total,
            "hallucinations_detected": hallucinations_detected,
            "hallucination_percentage": (hallucinations_detected / total) * 100 if total > 0 else 0,
            "avg_response_time_seconds": round(avg_response_time, 2),
            "total_tokens_used": total_tokens
        }

# Example usage
fact_checker = NewsFactChecker(api_key="YOUR_API_KEY")

article_text = """
Scientists at the University of Cambridge have discovered a new treatment for Alzheimer's 
disease that shows a 75% success rate in clinical trials. The revolutionary treatment,
based on neural regeneration therapy, could be available to patients as early as next year.
"""

trusted_sources = """
Recent Alzheimer's Research Updates (May 2025):
- University of Cambridge researchers are investigating a new approach to Alzheimer's treatment
  focusing on neural pathways, but clinical trials are still in Phase I.
- Current Alzheimer's treatments in late-stage trials show modest improvements in cognitive
  decline, with effectiveness rates between 15-30%.
- The FDA approval process for new Alzheimer's treatments typically takes 5-7 years after
  successful completion of Phase III trials.
"""

article_metadata = {
    "title": "Breakthrough in Alzheimer's Treatment",
    "source": "Health News Daily",
    "date": "2025-05-25",
    "author": "Jane Smith"
}

verification_result = fact_checker.verify_article_against_sources(
    article_text, trusted_sources, article_metadata
)

print(json.dumps(verification_result, indent=2))
print("\nVerification Statistics:")
print(json.dumps(fact_checker.get_verification_statistics(), indent=2))
```

## Best practices and tips

### Optimizing your context

The quality and relevance of your context have a significant impact on the accuracy of hallucination detection:

1. **Be comprehensive but concise** - Include all relevant information but avoid unnecessary details
2. **Structure your context** - Well-organized information makes it easier to verify claims
3. **Update regularly** - Ensure your context contains the most current information
4. **Include multiple viewpoints** - When appropriate, provide diverse perspectives for balanced verification

### Improving detection accuracy

1. **Start with clear prompts** - The clearer your original prompt, the better the agent can understand what to verify
2. **Provide sufficient context** - Include all information needed to verify claims
3. **Test with known examples** - Calibrate the system using examples with known hallucinations
4. **Use in conjunction with other techniques** - Combine with retrieval-augmented generation or fact-checking workflows

### Handling false positives and negatives

1. **Implement human review** - For critical applications, include human review of borderline cases
2. **Adjust thresholds** - In some cases, minor deviations from context might be acceptable
3. **Iterative refinement** - Use feedback to improve context and prompts over time

## Next steps

- **Question/Answer detection** - Learn how to [verify individual question-answer pairs](/get-started/hallucination-agent/question-answer/){target=_self}
- **Chat Completion detection** - Discover how to [validate responses in conversations](/get-started/hallucination-agent/chat-completion/){target=_self}
- **API reference** - Review the complete [API documentation](/api-reference/reference/){target=_blank} for all hallucination detection endpoints
- **Explore models** - Learn about our [Models](/get-started/models/){target=_blank} and their capabilities
