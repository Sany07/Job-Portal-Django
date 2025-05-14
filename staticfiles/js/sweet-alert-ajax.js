function call_sw_alert_func(route, id, message){
    // var CSRF_TOKEN = $('meta[name="csrf-token"]').attr('content');
    
    swal({
      title: "Are you sure?",
      text: message,
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {
        // var CSRF_TOKEN = `{{ csrf_token() }}`;
        // console.log(CSRF_TOKEN);
        $.ajax({
            type: 'GET',
            url: route,
            // data : {'_method' : 'DELETE', '_token' : CSRF_TOKEN },
            success : function(data) {
              if (route.includes('delete')) { 
                swal({
                  title: "Delete Done!",
                  text: "Your Job Was Deleted!",
                  icon: "success",
                  button: "Done",
                });
                $("#row_"+id).remove();
              }else if(route.includes('close')){
                swal({
                  title: "Done!",
                  text: "Your Job was marked closed!",
                  icon: "success",
                  button: "Done",
                });
                $("#change_job_status_"+id).html('<a class="text-white btn btn-success btn-sm" role="button">Closed</a>')
              }
            },

            error : function () {
                swal({
                    title: 'Something went wrong !',
                    // text: data.message,
                    timer: '1500'
                })
            }
        });
      } else {
        swal("Your Post Is Safe!");
      }
    });
  }