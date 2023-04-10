$.ajax({
    url: 'https://jsonplaceholder.typicode.com/posts',
    dataType: 'json',
    type: 'GET',
    data: {},
    success: function (data) {
        let sortedPosts = data.sort((a, b) => b.id - a.id)

        for (let i = 0; i < sortedPosts.length; i++) {
            let div = document.createElement('div');
            let userID = document.createElement('p');
            let postID = document.createElement('p');
            postID.setAttribute('id', `${data[i].id}`)
            let postTitle = document.createElement('p');
            postTitle.setAttribute('id', 'postTitle')
            let postBody = document.createElement('p');
            postBody.setAttribute('id', 'postBody')
            let space = document.createTextNode('\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0')


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
            div.appendChild(newLine.cloneNode())

            function editPost(event) {
                let editForm = document.createElement('form')
                editForm.setAttribute('name', 'editForm')
                editForm.setAttribute('method', 'post')
                editForm.setAttribute('action', 'submit')
                editForm.addEventListener('submit', savePost)

                let inputTitle = document.createElement('input')
                inputTitle.setAttribute('id', 'editTitle')
                inputTitle.setAttribute('name', 'New Title: ')
                inputTitle.setAttribute('placeholder', 'Enter new title')
                inputTitle.setAttribute('type', 'text')
                titleTag.innerHTML = 'Edit title: '
                editForm.appendChild(titleTag)
                editForm.appendChild(inputTitle)
                editForm.appendChild(newLine.cloneNode())
                editForm.appendChild(newLine.cloneNode())


                let inputBody = document.createElement('input')
                inputBody.setAttribute('id', 'editBody')
                inputBody.setAttribute('name', 'New Body: ')
                inputBody.setAttribute('placeholder', 'Enter new body')
                inputBody.setAttribute('type', 'text')
                bodyTag.innerHTML = 'Edit body: '
                editForm.appendChild(bodyTag)
                editForm.appendChild(inputBody)
                editForm.appendChild(newLine.cloneNode())


                let saveButton = document.createElement('button')
                // saveButton.setAttribute('type', 'submit')
                saveButton.setAttribute('id', 'saveButton')
                let buttonTag = document.createElement('label')
                buttonTag.innerHTML = 'Save'
                saveButton.appendChild(buttonTag)
                editForm.appendChild(saveButton)
                editForm.appendChild(newLine.cloneNode())
                editForm.appendChild(newLine.cloneNode())


                // saveButton.addEventListener('click', savePost)

                let postId = event.target.attributes.id.value
                let editedPost = document.getElementById(`${postId}`)
                editedPost.before(editForm)
            }

            // function deletePost(event) {
            //     let postId = event.target.attributes.value.id
            //     let node = document.getElementById(`${postId}`)
            //     if (node.parentNode) {
            //         node.parentNode.removeChild(node)
            //     }
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
