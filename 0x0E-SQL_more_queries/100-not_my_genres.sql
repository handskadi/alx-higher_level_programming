-- list all genres not linked to the show "Dexter"
SELECT `name` FROM `tv_genres`
WHERE `name` NOT IN (
	SELECT `name` FROM `tv_shows`
	INNER JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
	INNER JOIN `tv_genres` ON `tv_shows_genre`.`genre_id` = `tv_genres`.`id`
	WHERE `tv_shows`.`title` = "Dexter"
)
ORDER BY `name`;
