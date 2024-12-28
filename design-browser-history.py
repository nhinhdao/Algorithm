class Node():
    def __init__(self, url, prev = None, next = None):
        self.val = url
        self.prev = prev
        self.next = next

    def printSelf(self):
        prevVal = self.prev.val if self.prev else "None"
        nextVal = self.next.val if self.next else "None"
        print("curr " + self.val + " /prev " + prevVal+ " /next " + nextVal)

class BrowserHistory(object):
    def __init__(self, homepage):
        self.currentPage = Node(homepage, None, None)
        
    def visit(self, url):
        page = Node(url, self.currentPage, None)
        self.currentPage.next = page
        self.currentPage = page

    def back(self, steps):
        while steps > 0:
            lastPage = self.currentPage.prev
            self.currentPage = lastPage if lastPage else self.currentPage
            steps -= 1
        return self.currentPage.val
        

    def forward(self, steps):
        while steps > 0:
            nextPage = self.currentPage.next
            self.currentPage = nextPage if nextPage else self.currentPage
            steps -= 1
        return self.currentPage.val
    
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")       # You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com")     # You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1)                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1)                   # You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1)                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com")     # You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2)                # You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2)                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7)                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

print(browserHistory.currentPage.val)
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
