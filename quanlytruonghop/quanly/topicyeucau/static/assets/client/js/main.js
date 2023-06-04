// import 'jquery';

// LEFT SIDEBAR JS
$(document).on('click','#sidebar li', function(){
    $(this).addClass('active').siblings().removeClass('active')
});



// LEFT MENU SIDEBAR DP TOGGLE
$('.sub-menu ul').hide();
$(".sub-menu a").click(function(){
    $(this).parent(".sub-menu").children("ul").slideToggle("100");
    $(this).find(".right").toggleClass("fa-caret-up fa-caret-down");

})


//SIDEBAR TOGGLE
$(document).ready(function(){
    $("#toogleSidebar").click(function(){
        $(".left-menu").toggleClass("hide");
        $(".content-wrapper").toggleClass("hide");
    });
});





//Get start

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

// get the form, confirm-box and csrf token
const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
    const children = form.children
    console.log(children[0])
    for (let i=0; i < children.length; i++) {
        if(i <= size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
            // one.classList.add('checked')
            // two.classList.remove('checked')
            // three.classList.remove('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
            handleStarSelect(1)
            return
        }
        case 'second': {
            handleStarSelect(2)
            return
        }
        case 'third': {
            handleStarSelect(3)
            return
        }
        case 'fourth': {
            handleStarSelect(4)
            return
        }
        case 'fifth': {
            handleStarSelect(5)
            return
        }
        default: {
            handleStarSelect(0)
        }
    }

}

const getNumericValue = (stringValue) =>{
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1
    } 
    else if (stringValue === 'second') {
        numericValue = 2
    }
    else if (stringValue === 'third') {
        numericValue = 3
    }
    else if (stringValue === 'fourth') {
        numericValue = 4
    }
    else if (stringValue === 'fifth') {
        numericValue = 5
    }
    else {
        numericValue = 0
    }
    return numericValue
}

if (one) {
    const arr = [one, two, three, four, five]

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{
        // value of the rating not numeric
        const val = event.target.id
        
        let isSubmit = false
        form.addEventListener('submit', e=>{
            e.preventDefault()
            if (isSubmit) {
                return
            }
            isSubmit = true
            // picture id
            const id = e.target.id
            // value of the rating translated into numeric
            const val_num = getNumericValue(val)

            $.ajax({
                type: 'POST',
                url: '/rate/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'el_id': id,
                    'val': val_num,
                },
                success: function(response){
                    confirmBox.innerHTML = alert('Cảm ơn bạn đã đánh giá')
                },
                error: function(error){
                    confirmBox.innerHTML = alert('Có lỗi từ hệ thống')
                }
            })
        })
    }))
}


// Like article



// Notifications
const notification = [];
const listNotificationDOM = $("#notification-box");
const unreadNotificationDOM = $("#unread_notification");

function createNotificationItemDOM(e) {
    let time = new Date(e.create_at);
    return `
            <span class="message-item" id="notify-${e.id}">
                <div class="note-info-desmis">
                    <a href="${e.link}" class="user-notify-info mx-2 text-success">
                        <p class="note-name">${e.title}</p>
                        <p class="note-comment">${e.content}
                        </p>
                        <small class="text-muted text-info">${time.toLocaleTimeString()} ${time.toDateString()}</small>
                    </a>
                    <button class="btn btn-danger btn-sm" value="${e.id}" name="btn-remove">
                        <span class="fas fa-times"></span>
                    </button>
                </div>
            </span>
            `
}

function callRemoveNotification(id, callback) {

    let url = "http://127.0.0.1:8000/n/remove-notification/" + id;
    $.ajax({
        url: url,
        type: 'GET',
        success: callback
    });

}

function bindRemoveListenner() {
    $("button[name='btn-remove']").click(function(e) {
        let nId = $(this).val();
        console.log("btn remove clicked: " + nId);
        if(confirm('Xác nhận xóa bỏ thông báo?')) {
            callRemoveNotification(nId, (result) => {
                $(`#notify-${nId}`).remove();
                notification.length = 0;
                fetchNotifications();
            });
        }
    });
}

function addNotification(data) {
    
    if(notification.length === 0) {
        listNotificationDOM.empty();
    }
    notification.push(data);
    $(createNotificationItemDOM(data)).prependTo(listNotificationDOM);
    bindRemoveListenner();
}

const fetchNotifications = function() {
    $.get( "http://127.0.0.1:8000/n/get-list-notification/", function( data ) {
        notification.push(...data);
        if(notification.length > 0) {
            notification.forEach((e, i) => {
                $(createNotificationItemDOM(e)).prependTo(listNotificationDOM);
            });

            bindRemoveListenner();
        }
        else {
            $('<p class="text-danger text-center">Chưa có thông báo</p>').appendTo(listNotificationDOM);
        }
    });
}

$(document).ready(function() {
    fetchNotifications();
});


// End Notifications