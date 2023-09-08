# Function to calculate total memory allocated/deallocated by server 1
def calculate_memory_allocation(req_size, requests):
    memory_allocated = 0
    current_server = 1  # Start with server 1

    for req in requests:
        if current_server == 1:
            memory_allocated += req
        if req > 0:  # Positive request indicates allocation
            current_server = 3 - current_server  # Toggle between servers for allocation

    return memory_allocated

# Input
req_size = int(input())
requests = list(map(int, input().split()))

# Calculate and print the result
result = calculate_memory_allocation(req_size, requests)
print(result)
