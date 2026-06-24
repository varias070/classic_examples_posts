WITH items_data AS (
  SELECT * FROM UNNEST(
    %(book)s,
    %(quantity)s,
    %(price)s
  ) AS q (book, quantity, price)
),
total_cost AS (
  SELECT SUM(price) AS cost_sum FROM items_data
),
new_rental AS (
  INSERT INTO rental (cost, start_date, end_date, reader)
  SELECT cost_sum, %(start_date)s, %(end_date)s, %(reader)s
  FROM total_cost
  RETURNING id AS rental_id
),
updated_books AS (
  UPDATE book b
  SET quantity = GREATEST(b.quantity - i.quantity, 0)
  FROM items_data i
  WHERE b.id = i.book
    AND b.quantity >= i.quantity
  RETURNING b.id AS book_id, b.quantity AS new_quantity
)
INSERT INTO item (book, quantity, price, rental)
SELECT i.book, i.quantity, i.price, nr.rental_id
FROM items_data i, new_rental nr
RETURNING rental;