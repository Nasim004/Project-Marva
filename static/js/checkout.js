// $(document).ready(function() {

//     $('.payWithRazorpay').click(function(e){

//         e.preventDefault();




//         // var add = $("[name='address_id']").val();


//         // if(address_id == "")
//         // {   
//         //     swal(" Alert!","All fields are requried","error");
//         //     return false;
//         // }
//         // else
//         // {
//             $.ajax({
//                 method: "GET",
//                 url:"/proceed-to-pay",
//                 success: function(response){
  
//                     var options = {
//                         "key": "rzp_test_0kfcL6eczdRDZp", // Enter the Key ID generated from the Dashboard
//                         "amount": response.total*100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
//                         "currency": "INR",
//                         "name": "Nasim",
//                         "description": "Thankyou for buying",
//                         "image": "https://example.com/your_logo",
//                         // "order_id": "order_IluGWxBm9U8zJ8", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
//                         "handler": function (response){
//                             alert(response.razorpay_payment_id);
//                         },
//                         "prefill": {
//                             "name": "Hii",
                         
//                         },
//                         "notes": {
//                             "address": "Razorpay Corporate Office"
//                         },
//                         "theme": {
//                             "color": "#3399cc"
//                         }
//                     };
//                     var rzp1 = new Razorpay(options);
//                     rzp1.open( );
//             }
        

//             });   
//         // }
//     });

    







    // $(document).ready(function() {
    //     $('.payWithRazorpay').click(function (e) { 
    //         var amount = $('#addd').val()
    //         var cart = $('#cart').val()
    //         var address = $('#address').val()
    //         var payment = "Razorpay"
    //         var token = $("input[name='csrfmiddlewaretoken']").val()
    //         e.preventDefault();
    //         $.ajax({
    //             type: "GET",
    //             url: "/razorpay",
    //             success: function (response) {
    //                 console.log(response);
    //                 var options={
    //                     "key": "rzp_test_z8aKggxY5VTzKH", // Enter the Key ID generated from the Dashboard
    //                     "amount": 1*100,//response.total, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    //                     "currency": "INR",
    //                     "name": "cart",
    //                     "description": "Thank you for shopping with us",
    //                     "image": "https://example.com/your_logo",
    //                     // "order_id": response.id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
    //                     "handler": function (response){
    //                         // alert(response.razorpay_payment_id);
    //                         data = {
    //                             "razorpay_payment_id": response.razorpay_payment_id,
    //                             "amount" : amount,
    //                             "cart" : cart,
    //                             "address" : address,
    //                             "payment" : payment,
    //                             csrfmiddlewaretoken: token
    //                         }
    //                         $.ajax({
    //                             type: "POST",
    //                             url: "/payment",
    //                             data: data,
    //                             success: function (responsec) {
    //                                 swal("Congratulations!", responsec.status, "success").then((value) => {
    //                                     window.location.href = "/myorder"
    //                                 });
    //                             }
    //                         });
    //                     },
    //                     "prefill": {
    //                         "name": "Gaurav Kumar",
    //                         "email": "",
    //                         "contact": "9999999999",
    //                     },
    //                     "notes": {
    //                         "address": "Razorpay Corporate Office"
    //                     },
    //                     "theme": {
    //                         "color": "#3399cc"
    //                     },
    //                 };
    //                 var rzp1 = new Razorpay(options);
    //                 rzp1.open();
    //             }
    //         });
    //     });
    // });













    
    //   $(document).ready(function() {
    //     $('#rzp-button1').click(function (e) { 
    //       var address = $('#addd').val()
    //       alert("sdfsf")
    //       var payment = "Razorpay"
    //         var token = $("input[name='csrfmiddlewaretoken']").val()
    //         e.preventDefault();
    //         $.ajax({
    //             type: "GET",
    //             url: "/razorpay",
    //             success: function (response) {
    //                 console.log(response);
    //                 console.log(response.total);
    //                 var options={
    //                     "key": "rzp_test_0kfcL6eczdRDZp", // Enter the Key ID generated from the Dashboard
    //                     "amount": response.total*100,//response.total, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    //                     "currency": "INR",
    //                     "name": "cart",
    //                     "description": "Thank you for shopping with us",
    //                     "image": "https://example.com/your_logo",
    //                     // "order_id": response.id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
    //                     "handler": function (response){
    //                         // alert(response.razorpay_payment_id);
    //                         data = {
    //                             "razorpay_payment_id": response.razorpay_payment_id,
    //                             "addressaddress_id" : address,
    //                             "payment_selector" : payment,
    //                             'csrfmiddlewaretoken': token
    //                         }
    //                         $.ajax({
    //                             type: "POST",
    //                             url: "/checkout",
    //                             data: data,
    //                             success: function (responsec) {
    //                                 console.log("enter----")
    //                                 swal("Congratulations!", responsec.status, "success").then((value) => {
    //                                     window.location.href = "orderplaced"
    //                                 });
    //                             }
    //                         });
    //                     },
    //                     "prefill": {
    //                         "name": "Gaurav Kumar",
    //                         "email": "",
    //                         "contact": "9999999999",
    //                     },
    //                     "notes": {
    //                         "address": "Razorpay Corporate Office"
    //                     },
    //                     "theme": {
    //                         "color": "#3399cc"
    //                     },
    //                 };
    //                 var rzp1 = new Razorpay(options);
    //                 rzp1.open();
    //             }
    //         });
    //     });
    // });
    