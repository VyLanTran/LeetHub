# Write your MySQL query statement below

# select distinct v1.viewer_id as id
# from views v1
# join views v2
# on v1.viewer_id = v2.author_id
# order by v1.viewer_id;

select distinct author_id as id
from views
where author_id = viewer_id
order by id;