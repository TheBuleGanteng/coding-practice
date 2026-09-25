'''
Problem 1 (easy) — Top error sources. You're given a list of log lines, each a string "timestamp|source|level|message", e.g. "2026-09-24T10:00:00|api-gateway|ERROR|timeout". Write top_error_sources(logs, k) returning the k sources with the most ERROR-level lines, most to fewest; ties broken alphabetically. When it works, say aloud: what's the time complexity in terms of n (number of lines)? And what happens if a line is malformed — make it survive that.
'''

def top_error_sources(logs, k):
    
    # Declare a new dict (let's call it "sorted_data") that has the format source: <source name>, count: <number of times source appears>
    unsorted_data = {}
    
    for line in logs: # Iterate across each of the lines in the logs list
            
        parts = line.split("|") # Parse each line by the "|" char
        if len(parts) != 4: # Malformed line, skip
            continue
        
        source, level = parts[1], parts[2] # Extract the source [1] and the message type [2]
        if level == "ERROR":
            unsorted_data[source] = unsorted_data.get(source, 0) + 1 # look in sorted_data to see if source is there. If not, add it with a 0 value. Then, in either case, increment the value by 1
                                  
    sorted_data = sorted(unsorted_data.items(), key=lambda kv: (-kv[1], kv[0])) # Sort w/ count as primary key (in reverse / decending order) and source name as secondary key                             
    return [source for source, _ in sorted_data[:k]]
        

    # Question: What is time complexity in terms of n (number of lines)?
    # Answer: The time complexity to run would be n (e.g the loop runs once for each line in the list) and then add some marginal additional time (less than n) for sorting