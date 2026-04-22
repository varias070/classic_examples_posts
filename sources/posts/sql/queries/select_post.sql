SELECT
   id       AS Post__id,
   title    AS Post__title,
   text     AS Post__text,
   channel_id AS Post__channel_id
FROM post
WHERE id = %(id)s;
