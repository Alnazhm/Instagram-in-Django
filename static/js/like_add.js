


    $('#btn-to-like').on('click', function (evt) {
        const pk = $('button[data-pk]').data('pk')
        evt.preventDefault()


        // $('#form-to-like').remove()
        likeForm = $('#form-to-like[data-pk]')
        likeForm[0].style.display = 'none'

        disForm = $('#form-to-dislike[data-pk]')
        disForm[0].style.display = 'block'


        let url = '';
        $.ajax({
            type: 'POST',
            url : `http://localhost:8000/posts/like/${pk}/`,
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action:'post',
            },
            success: function(data) {

                alert(`Лайк  ${pk} добавлен!`)
            }
        })
    })



    $('#btn-to-dislike').on('click', function (evt) {
        const pk = $('button[data-pk]').data('pk')
        evt.preventDefault()

        dislikeForm = $('#form-to-dislike[data-pk]')
        dislikeForm[0].style.display = 'none'

        likeForm = $('#form-to-like[data-pk]')
        console.log(likeForm[0])
        likeForm[0].style.display = 'block'
        likeForm.display()


        let url = 'http://localhost:8000/posts/';
        $.ajax({
            type: 'POST',
            url : `http://localhost:8000/posts/like/${pk}`,
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action:'post',
            },
            success: function(data) {

                alert(`Лайк  ${pk} удалён!`)
            }
        })
    })



