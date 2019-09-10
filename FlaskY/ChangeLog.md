## Change History

_**20190210**_
* draft version


_**20190213**_
* 将配置信息从代码中剥离到单独的settings.py中
* 考虑到我的文章标题多是中文的，现有的生成slug的机制不太合适，换了一种方案。
* 增加收藏夹图标
* Add a User model and store usernames and hashed passwords in the database, then use these Users to improve the authentication system.

_**20190213**_
* Add support for image uploads and a way to easily embed them in your entries. You can even just upload them then generate a markdown image link!


_**Someday I will implement**_
* Allow entries to have tags and create URLs for browsing by tag (kinda like this page).
* Add tag based navigation panel on the left side.
* Add a comments section to each entry. Comments should be stored in a separate model that relates back to an Entry. You can display a form on the bottom of each Entry detail page and have it POST to a special view that creates a new comment.
* Add a contact form that sends email messages. Bonus points for adding spam detection to this form.
* If you anticipate lots of traffic, you might investigate ways to cache static parts of the site.
* Use SQLCipher to keep your database encrypted!
* Add an RSS feed to your site.