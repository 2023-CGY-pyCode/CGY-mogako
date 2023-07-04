from collections import Counter

N = int(input())  

books = []
for _ in range(N):
    book = input()  
    books.append(book)

book_counts = Counter(books)

best_selling_books = sorted(book_counts.items(), key=lambda x: (-x[1], x[0]))

print(best_selling_books[0][0])