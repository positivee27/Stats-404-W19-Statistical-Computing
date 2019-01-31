# import pandas as pd
#
# tmp = pd.Series([3, 5, -1])
# tmp.values
# tmp.index


albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track

who were the top3 most purchased artist in CA each year

1. select from artists (artist ID, name)

See (some) artists that are in database:
select * from artists limit 10;

See which AC/DC albums are in database:
select * from albums where artistid = 1;

See range of invoice dates:
select min(invoicedate), max(invoicedate) from invoices;

See what states the customers are from:
select distinct(state) from customers order by state;


2. the most purchase: invoice_items(quantity)
3. in CA: invoices