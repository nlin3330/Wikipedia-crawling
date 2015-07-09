import wikipedia
import json

class FifoQueue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def wikibfs(start):
    pagesVisited = set()
    invalidLinks = set()
    pagesToVisit = FifoQueue()
    pagesToVisit.push(start)
    counter = 0
    outputfilenum = 1
    currPages = {}
    while not pagesToVisit.isEmpty():
        title = pagesToVisit.pop()
        if title in pagesVisited or title in invalidLinks:
            continue
        try:
            currentPage = wikipedia.WikipediaPage(title)
            pagesVisited.add(title)
            link =  currentPage.links
            if(counter < 1000):
                counter += 1
                currPages[title] = link
            else:
                counter = 0
                with open('data/outputfile' + str(outputfilenum)+'.json','w') as outfile:
                    json.dump(currPages,outfile)
                currPages = {}
                currPages[title] = link
                outputfilenum += 1
            for l in link:
                if l not in pagesVisited:
                     pagesToVisit.push(l)
        except:
            invalidLinks.add(title)
            continue

    wikipediaPages = list(pagesVisited)
    with open('wikipediaPages.json' , 'w') as outfile:
        json.dump(wikipediaPages,outfile)

wikibfs('Abraham Lincoln')
