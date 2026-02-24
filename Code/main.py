from agents.filing_agent import analyze_filing

#load filing text 
with open("code/data/apple_filing.txt", "r", encoding = "utf-8") as f:
    filing_text = f.read()

#run filing agent
result = analyze_filing(filing_text)

print(result)



