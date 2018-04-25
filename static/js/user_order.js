    var deleteOrder = false;
    var deleteOrderid = 0;

    $(function(){
        $("a[orderStatus]").click(function(){
            var orderStatus = $(this).attr("orderStatus");
            if('all'==orderStatus){
                $("table[orderStatus]").show();
            }
            else{
                $("table[orderStatus]").hide();
                $("table[orderStatus="+orderStatus+"]").show();
            }

            $("div.orderType div").removeClass("selectedOrderType");
            $(this).parent("div").addClass("selectedOrderType");
        });

        $("a.deleteOrderLink").click(function(){
            deleteOrderid = $(this).attr("oid");
            deleteOrder = false;
            $("#deleteConfirmModal").modal("hide");
        });

        $("button.deleteConfirmButton").click(function(){
            deleteOrder = true;
            $("#deleteConfirmModal").modal('hide');
        });

        $('#deleteConfirmModal').on('hidden.bs.modal', function (e) {
            if(deleteOrder){
                var page="foredeleteOrder";
                /*if(false)$.post(
                        page,
                        {"oid":deleteOrderid},
                        function(result){
                            if("success"==result){
                                $("table.orderListItemTable[oid="+deleteOrderid+"]").hide();
                            }
                            else{
                                location.href="login.jsp";
                            }
                        }
                    );*/
            }
        })
        $(".ask2delivery").click(function(){
            var link = $(this).attr("link");
            $(this).hide();
            page = $('#now_url').val();
            $.ajax({
                   url: page,
                   success: function(result){
                       alert("卖家已秒发，刷新当前页面，即可进行确认收货")
                   }
                });

        });
    });
    //<script href="{% static 'js/user_order.js' %}"></script>