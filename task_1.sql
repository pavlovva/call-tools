SELECT a.id, a.title
FROM article a
LEFT JOIN comment c ON a.id = c.article_id
WHERE c.article_id IS NULL;