Tasks
0. cURL body size
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

The size must be displayed in bytes
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

1. cURL to the end
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

Display only body of a 200 status code response
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000
    
2. cURL Method
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000
    
3. cURL only methods
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
    
4. cURL headers
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

A header variable X-School-User-Id must be sent with the value 98
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000
    
5. cURL POST parameters
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

A variable email must be sent with the value test@gmail.com
A variable subject must be sent with the value I will always be here for PLD
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000
    
6. Find a peak
mandatory
Score: 0.0% (Checks completed: 0.0%)
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

    
7. Only status code

Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

You are not allowed to use any pipe, redirection, etc.
You are not allowed to use ; and &&
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000
    
8. cURL a JSON file

Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
You have to use curl
Please test your scripts in the sandbox provided, using the web server running on port 5000

9. Catch me if you can!
Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

You have to use curl
You are not allow to use echo, cat, etc. to display the final result
Please test your script in the sandbox provided, using the web server running on port 5000

