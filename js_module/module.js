$.ajax({
    url: 'https://jsonplaceholder.typicode.com/posts',
    dataType: 'json',
    type: 'GET',
    data: {},
    success: function (data) {
        let sortedPosts = data.sort((a, b) => b.id - a.id)

        for (let i = 0; i < sortedPosts.length; i++) {
            let div = document.createElement('div');
            div.setAttribute('id', `${data[i].id}`)
            div.setAttribute('title', 'post')
            let userID = document.createElement('p');
            userID.setAttribute('id', `userId`)
            userID.hidden = true
            let postID = document.createElement('p');
            postID.setAttribute('id', `postId`)
            postID.hidden = true
            let postTitle = document.createElement('p');
            postTitle.setAttribute('id', 'postTitle')
            let postBody = document.createElement('p');
            postBody.setAttribute('id', 'postBody')
            let space = document.createTextNode('\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0')
            let comments = document.createElement('div')
            comments.setAttribute('id', 'comments')


            let editButton = document.createElement('button')
            editButton.setAttribute('id', 'editBtn')
            editButton.setAttribute('type', 'submit')
            editButton.addEventListener('click', editPost)
            editButton.innerHTML = 'Edit'


            let deleteButton = document.createElement('button')
            deleteButton.setAttribute('id', 'deleteBtn')
            deleteButton.setAttribute('type', 'submit')
            deleteButton.addEventListener('click', deletePost)
            deleteButton.innerHTML = 'Delete'

            let commentsButton = document.createElement('button')
            commentsButton.setAttribute('id', 'commentsBtn')
            commentsButton.addEventListener('click', changeStateComments)
            commentsButton.innerHTML = 'Comments'

            let addCommentButton = document.createElement('button')
            addCommentButton.setAttribute('id', 'addCommentBtn')
            addCommentButton.addEventListener('click', createNewCommentForm)
            addCommentButton.innerHTML = 'Add comment'

            userID.innerHTML = `User ID: ${sortedPosts[i].userId}`;
            postID.innerHTML = `Post ID: ${sortedPosts[i].id}`;
            postTitle.innerHTML = `Title: ${sortedPosts[i].title}`;
            postBody.innerHTML = `Body: ${sortedPosts[i].body}`;
            document.body.appendChild(div)

            div.appendChild(newLine.cloneNode())
            div.appendChild(userID)
            div.appendChild(postID)
            div.appendChild(postTitle)
            div.appendChild(postBody)
            div.appendChild(editButton)
            div.append(space)
            div.appendChild(deleteButton)
            div.append(space)
            div.appendChild(commentsButton)
            div.append(space)
            div.appendChild(addCommentButton)
            div.appendChild(comments)
            div.appendChild(newLine.cloneNode())

            function editPost(event) {
                let parentDiv = event.target.parentNode
                let postTitle = parentDiv.querySelector("#postTitle")
                let postBody = parentDiv.querySelector("#postBody")
                let deleteBtn = parentDiv.querySelector("#deleteBtn")

                event.target.hidden = true
                deleteBtn.hidden = true
                postTitle.hidden = true
                postBody.hidden = true

                let editForm = document.createElement('form')
                editForm.setAttribute('name', 'editForm')
                editForm.setAttribute('method', 'post')
                editForm.setAttribute('action', 'submit')
                editForm.setAttribute('id', 'editForm')
                editForm.addEventListener('submit', saveEditedPost)

                let inputTitle = document.createElement('textarea')
                inputTitle.setAttribute('id', 'editTitle')
                inputTitle.setAttribute('name', 'New Title: ')
                inputTitle.setAttribute('placeholder', 'Enter new title')
                inputTitle.setAttribute('type', 'text')
                inputTitle.value = postTitle.innerHTML.slice(7)
                titleTag.innerHTML = 'Edit title: '
                editForm.appendChild(titleTag)
                editForm.appendChild(inputTitle)
                editForm.appendChild(newLine.cloneNode())
                editForm.appendChild(newLine.cloneNode())


                let inputBody = document.createElement('textarea')
                inputBody.setAttribute('id', 'editBody')
                inputBody.setAttribute('name', 'New Body: ')
                inputBody.setAttribute('placeholder', 'Enter new body')
                inputBody.setAttribute('type', 'text')
                inputBody.value = postBody.innerHTML.slice(6)
                bodyTag.innerHTML = 'Edit body: '
                editForm.appendChild(bodyTag)
                editForm.appendChild(inputBody)
                editForm.appendChild(newLine.cloneNode())

                let saveButton = document.createElement('button')
                saveButton.setAttribute('type', 'submit')
                saveButton.setAttribute('id', 'saveButton')
                let buttonTag = document.createElement('label')
                buttonTag.innerHTML = 'Save'
                saveButton.addEventListener('click', saveEditedPost)
                saveButton.appendChild(buttonTag)
                editForm.appendChild(saveButton)
                editForm.appendChild(newLine.cloneNode())
                editForm.appendChild(newLine.cloneNode())

                parentDiv.appendChild(editForm)
            }

            function deletePost(event) {
                let parentDiv = event.target.parentNode
                // TODO: put here request to the backend
                parentDiv.remove()
            }
        }
    },
    error: function (jqXHR, textStatus, errorThrown) {
        console.log("Error: " + textStatus + " " + errorThrown);
    }
})


const title = document.createElement('h1')
title.setAttribute('id', 'postsTitle')
title.innerText = 'Posts'

let newLine = document.createElement('br')
let titleTag = document.createElement('label')
let bodyTag = document.createElement('label')
let buttonTag = document.createElement('label')

const newPost = document.createElement('h2')
newPost.setAttribute('id', 'newPost')
newPost.innerText = 'New Post'

document.body.appendChild(title)
document.body.appendChild(newPost)

const newPostForm = document.createElement('form')
newPostForm.setAttribute('name', 'newPostForm')
newPostForm.setAttribute('method', 'post')
newPostForm.setAttribute('action', 'submit')
newPostForm.addEventListener('submit', savePost)
document.getElementsByTagName('body')[0].appendChild(newPostForm)

const inputTitle = document.createElement('input')
inputTitle.setAttribute('id', 'newTitle')
inputTitle.setAttribute('name', 'New Title: ')
inputTitle.setAttribute('placeholder', 'Enter post title')
inputTitle.setAttribute('type', 'text')
titleTag.innerHTML = 'New title: '

const inputBody = document.createElement('textarea')
inputBody.setAttribute('id', 'newBody')
inputBody.setAttribute('name', 'New Body: ')
inputBody.setAttribute('placeholder', 'Enter post body')
inputBody.setAttribute('type', 'text')
bodyTag.innerHTML = 'New body: '

const formButton = document.createElement('button')
formButton.setAttribute('type', 'submit')
formButton.setAttribute('id', 'formButton')
buttonTag.innerHTML = 'Save post'
formButton.addEventListener('click', savePost)
formButton.appendChild(buttonTag)

newPostForm.appendChild(titleTag)
newPostForm.appendChild(newLine.cloneNode())
newPostForm.appendChild(inputTitle)
newPostForm.appendChild(newLine.cloneNode())
newPostForm.appendChild(newLine.cloneNode())

newPostForm.appendChild(bodyTag)
newPostForm.appendChild(newLine.cloneNode())
newPostForm.appendChild(inputBody)
newPostForm.appendChild(newLine.cloneNode())
newPostForm.appendChild(newLine.cloneNode())

newPostForm.appendChild(formButton)
newPostForm.appendChild(newLine.cloneNode())
newPostForm.appendChild(newLine.cloneNode())


// load usernames
$.ajax({
    url: 'https://jsonplaceholder.typicode.com/users',
    dataType: 'json',
    type: 'GET',
    data: {},
    success: function (data) {

        let nameIdPairs = {}
        for (let i = 0; i < data.length; i++) {
            nameIdPairs[`${data[i].id}`] = data[i].username
        }

        let posts = document.querySelectorAll('[title="post"]')
        for (let i = 0; i < posts.length; i++) {
            let post = posts[i]
            let userIdEl = post.querySelector("#userId")
            if (userIdEl) {
                let userId = userIdEl.innerHTML.slice(9)

                let userNameEl = document.createElement('p')
                userNameEl.setAttribute('id', `userName`)
                userNameEl.innerHTML = nameIdPairs[userId]
                let postBody = post.querySelector('#postBody')
                userNameEl.style.cssFloat = 'right'
                postBody.after(userNameEl)
            }
        }
    },
    error: function (jqXHR, textStatus, errorThrown) {
        console.log("Error: " + textStatus + " " + errorThrown);
    }
})


// load comments
$.ajax({
    url: 'https://jsonplaceholder.typicode.com/comments',
    dataType: 'json',
    type: 'GET',
    data: {},
    success: function (data) {

        for (let i = 0; i < data.length; i++) {
            let row = data[i]
            let postDiv = document.getElementById(`${row.postId}`)
            let comments = postDiv.querySelector('#comments')
            
            let commentDiv = document.createElement('div')
            commentDiv.setAttribute('id', `comment${row.id}`)
            let commentName = document.createElement('p')
            commentName.setAttribute('id', 'commentName')
            commentName.innerHTML = `Name: ${row.name}`
            let commentEmail = document.createElement('p')
            commentEmail.setAttribute('id', 'commentEmail')
            commentEmail.innerHTML = `Email: ${row.email}`
            let commentBody = document.createElement('p')
            commentBody.setAttribute('id', 'commentBody')
            commentBody.innerHTML = `Comment: ${row.body}`

            commentDiv.appendChild(newLine.cloneNode())
            commentDiv.appendChild(commentName)
            commentDiv.appendChild(commentEmail)
            commentDiv.appendChild(commentBody)

            comments.appendChild(commentDiv)
        }

        let posts = document.querySelectorAll('[title="post"]')
        for (let i = 0; i < posts.length; i++) {
            let comments = posts[i].querySelector('#comments')
            comments.style.display = 'none'
        }
    },
    error: function (jqXHR, textStatus, errorThrown) {
        console.log("Error: " + textStatus + " " + errorThrown);
    }
})

function savePost(event) {
    let newTitle = document.getElementById('newTitle')
    let newBody = document.getElementById('newBody')

    if (newTitle.value === '' || newBody.value === '') {
        alert('Ensure you filled in both fields.')
    } else {
        let newPost = document.createElement('div');
        let newPostTitle = document.createElement('p')
        newPostTitle.innerHTML = newTitle.value
        newPost.appendChild(newPostTitle)
        let newPostBody = document.createElement('p')
        newPostBody.innerHTML = newBody.value
        newPost.appendChild(newPostBody)

        let firstPost = document.getElementsByTagName('div')[0]
        firstPost.before(newPost)

    }

}

function saveEditedPost(event) {
    let parentDiv = event.target.parentNode.parentNode.parentNode

    let newTitle = parentDiv.querySelector('#editTitle')
    let newBody = parentDiv.querySelector('#editBody')

    let postTitle = parentDiv.querySelector("#postTitle")
    let postBody = parentDiv.querySelector("#postBody")
    let editBtn = parentDiv.querySelector("#editBtn")
    let deleteBtn = parentDiv.querySelector("#deleteBtn")

    let form = parentDiv.querySelector("#editForm")

    // TODO: put here request to the backend
    postTitle.innerHTML = `Title: ${newTitle.value}`;
    postBody.innerHTML = `Body: ${newBody.value}`;

    editBtn.hidden = false
    deleteBtn.hidden = false
    postTitle.hidden = false
    postBody.hidden = false

    form.remove()
}

function changeStateComments(event) {
    let parentDiv = event.target.parentNode
    let comments = parentDiv.querySelector('#comments')

    if (comments.style.display !== 'none') {
        comments.style.display = 'none';
    }
    else {
        comments.style.display = 'block';
    }
}

function createNewCommentForm(event) {
    let parentDiv = event.target.parentNode
    console.log(parentDiv)

    let commentForm = document.createElement('form')
    commentForm.setAttribute('name', 'newCommentForm')
    commentForm.setAttribute('method', 'post')
    commentForm.setAttribute('action', 'submit')
    commentForm.setAttribute('id', 'newCommentForm')
    commentForm.addEventListener('submit', saveNewComment)

    let commentName = document.createElement('input')
    commentName.setAttribute('id', 'newCommentName')
    commentName.setAttribute('name', 'Name: ')
    commentName.setAttribute('placeholder', 'Enter comment name')
    commentName.setAttribute('type', 'text')
    commentForm.appendChild(commentName)
    commentForm.appendChild(newLine.cloneNode())
    commentForm.appendChild(newLine.cloneNode())

    let commentEmail = document.createElement('input')
    commentEmail.setAttribute('id', 'newCommentEmail')
    commentEmail.setAttribute('name', 'Email: ')
    commentEmail.setAttribute('placeholder', 'Enter your email')
    commentEmail.setAttribute('type', 'text')
    commentForm.appendChild(commentEmail)
    commentForm.appendChild(newLine.cloneNode())
    commentForm.appendChild(newLine.cloneNode())


    let commentBody = document.createElement('textarea')
    commentBody.setAttribute('id', 'newCommentBody')
    commentBody.setAttribute('name', 'Comment Body: ')
    commentBody.setAttribute('placeholder', 'Enter comment')
    commentBody.setAttribute('type', 'text')
    commentForm.appendChild(commentBody)
    commentForm.appendChild(newLine.cloneNode())

    let saveButton = document.createElement('button')
    saveButton.setAttribute('type', 'submit')
    saveButton.setAttribute('id', 'saveCommentButton')
    let buttonTag = document.createElement('label')
    buttonTag.innerHTML = 'Save'
    saveButton.addEventListener('click', saveNewComment)
    saveButton.appendChild(buttonTag)
    commentForm.appendChild(saveButton)

    let cancelButton = document.createElement('button')
    cancelButton.setAttribute('type', 'submit')
    cancelButton.setAttribute('id', 'cancelCommentButton')
    let cancleButtonTag = document.createElement('label')
    cancleButtonTag.innerHTML = 'Cancel'
    cancelButton.addEventListener('click', cancelNewComment)
    cancelButton.appendChild(cancleButtonTag)
    commentForm.appendChild(cancelButton)

    parentDiv.appendChild(commentForm)
}

function saveNewComment(event) {
    let parentDiv = event.target.parentNode.parentNode.parentNode
    console.log(parentDiv)

    let comments = parentDiv.querySelector('#comments')

    let newCommentName = parentDiv.querySelector('#newCommentName')
    let newCommentEmail = parentDiv.querySelector('#newCommentEmail')
    let newCommentBody = parentDiv.querySelector('#newCommentBody')

    let commentDiv = document.createElement('div')
    let commentName = document.createElement('p')
    commentName.setAttribute('id', 'commentName')
    commentName.innerHTML = `Name: ${newCommentName.value}`
    let commentEmail = document.createElement('p')
    commentEmail.setAttribute('id', 'commentEmail')
    commentEmail.innerHTML = `Email: ${newCommentEmail.value}`
    let commentBody = document.createElement('p')
    commentBody.setAttribute('id', 'commentBody')
    commentBody.innerHTML = `Comment: ${newCommentBody.value}`

    commentDiv.appendChild(newLine.cloneNode())
    commentDiv.appendChild(commentName)
    commentDiv.appendChild(commentEmail)
    commentDiv.appendChild(commentBody)

    comments.prepend(commentDiv)

    let commentForm = parentDiv.querySelector('#newCommentForm')
    commentForm.remove()
}

function cancelNewComment(event) {
    let parentDiv = event.target.parentNode.parentNode
    parentDiv.remove()
}
