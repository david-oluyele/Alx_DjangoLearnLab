# Blog Post Management

## Features
- **Create**: Authenticated users can create new blog posts.
- **Read**: All users can view a list of posts or individual post details.
- **Update**: Only the author of a post can edit it.
- **Delete**: Only the author of a post can delete it.

## Permissions
- **Authenticated users** can create, edit, and delete posts.
- **Only the author** can edit or delete their own posts.

## Testing
Test each view to ensure the correct functionality of CRUD operations and permissions.

# Django Blog - Comment System
This README section describes the implementation of the comment functionality added to the blog project. The comment system allows users to post comments on blog posts, and authenticated users can edit or delete their own comments.

## Features
Add Comments: Authenticated users can post comments on blog posts.
Edit Comments: Users can edit their own comments.
Delete Comments: Users can delete their own comments.
View Comments: All users can view comments associated with a specific blog post.
How It Works
The comment system is integrated into the blog post detail page, allowing users to:

See a list of all comments under each blog post.
Post new comments if they are authenticated.
Edit or delete their own comments if they are the author.
Comment Model
The Comment model stores information related to each comment:

post: The blog post the comment is associated with (foreign key to the Post model).
author: The user who wrote the comment (foreign key to Django’s built-in User model).
content: The text of the comment.
created_at: Timestamp when the comment was created.
updated_at: Timestamp when the comment was last updated.
Comment Views
CommentCreateView: Allows authenticated users to create a comment for a post.
CommentUpdateView: Allows users to edit their own comments.
CommentDeleteView: Allows users to delete their own comments.
Comment Forms
The CommentForm is used to create and update comments. It is a Django ModelForm for the Comment model, which includes the content of the comment.

# URL Patterns
The comment-related actions are mapped to the following URL patterns:

Create a comment: /posts/<int:post_id>/comments/new/
Edit a comment: /posts/<int:post_id>/comments/<int:pk>/edit/
Delete a comment: /posts/<int:post_id>/comments/<int:pk>/delete/
Permissions
Only authenticated users can add, edit, or delete comments.
Users can only edit or delete comments they have authored.
All users can view comments on blog posts.

# How to Use
Adding a Comment
Log in to your account.
Navigate to a blog post.
Scroll to the comment section at the bottom of the post.
Enter your comment in the provided text field and click "Save Comment" to post it.
Editing a Comment
Navigate to the post where your comment is located.
Click the "Edit" button next to your comment.
Modify the content of your comment and click "Save Comment".
Deleting a Comment
Navigate to the post where your comment is located.
Click the "Delete" button next to your comment.
Confirm the deletion in the prompt to remove the comment permanently.
Testing
Test the comment system by:

Creating new comments and verifying they are saved under the correct post.
Editing comments and ensuring only the comment author can do so.
Deleting comments and confirming that only the comment author can delete them.
Ensuring all comments are displayed correctly on the post detail page.

# Conclusion
The comment functionality allows users to engage with blog posts by leaving feedback, which enhances interactivity and community involvement.

