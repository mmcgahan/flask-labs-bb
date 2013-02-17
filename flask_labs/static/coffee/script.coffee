jQuery ->
    buy_item = (id, $checkbox) ->
        $.ajax({
            type: 'POST'
            url: document.URL
            data: JSON.stringify(id: id)
            dataType: 'json'
            contentType: 'application/json'
            success: (response) ->
                $checkbox.prop("checked", true).prop('disabled', true).parents('tr').addClass('bought')
                response.response
            error: (jqXHR, textStatus, errorThrown) ->
                $('body').html(errorThrown + ' responseText: ' + jqXHR.responseText)
                false
        })
        true

    $('.buy-item').click (e) ->
        e.preventDefault()
        if window.confirm("Are you sure you want to mark this book as 'Gifted'? This action cannot be undone")
            buy_item $(this).data('id'),$(this)
        true

    $('#home-logo').click () ->
        window.location = 'http://' + window.location.host
        true

    true
