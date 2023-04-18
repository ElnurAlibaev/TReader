'''
with open('books/books_final_2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:

        book = Book(title=row['title'], image=row['image'], score=row['total_score'], release_date=row['release_date'],
                    description=row['description'], book_type=row['book_type'])
        book.save()

        genres = row['genres'].replace('[', '').replace(']', '').replace('\'', '')
        genres = [g.strip() for g in genres.split(',')]

        tags = row['tags'].replace('[', '').replace(']', '').replace('\'', '')
        tags = [t.strip() for t in tags.split(',')]

        for genre in genres:
            try:
                genre = Genre.objects.get(title=genre)
            except:
                genre = Genre(title=genre)
                genre.save()

            finally:
                book.genres.add(genre)

        for tag in tags:
            try:
                tag = Tag.objects.get(title=tag)
            except:
                tag = Tag(title=tag)
                tag.save()

            finally:
                book.tags.add(tag)

        s1 = Source(book=book, title='Mangalib', chapters=row['mangalib_chapters'], link=row['mangalib_link'])
        s2 = Source(book=book, title='ReadManga', chapters=row['readmanga_chapters'], link=row['readmanga_link'])
        s3 = Source(book=book, title='ReManga', chapters=row['remanga_chapters'], link=row['remanga_link'])
        s1.save()
        s2.save()
        s3.save()
'''
