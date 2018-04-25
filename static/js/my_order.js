
cg_btn = function(){
    var status = $('#status').val();
    alert(status)
    if (status == 'waitPay'){
       $('#ope_btn').html('付款');
    }
    else if(status == 'waitDelivery'){
       $('#ope_btn').html('查看物流')
    }
    else if(status == 'waitConfirm'){
       $('#ope_btn').html('确认收货')
    }
    else if(status == 'finish'){
       $('#ope_btn').html('去评价')
    }
};
window.onload=function(){//用window的onload事件，窗体加载完毕的时候
    cg_btn();
};
go_btn = function () {
    var ope_btn_val = $('#ope_btn').html();
    alert(ope_btn_val);
    if (ope_btn_val == '付款'){
        $('#form_gp').submit();
    }
    if (ope_btn_val == '查看物流'){
        var gg_url = $('#form_gg').attr('href')
        var order_code = $('#order_code').val()
        $.get(gg_url,{'order_code':order_code},function () {
            cg_btn();
        })
    }
    if (ope_btn_val == '确认收货'){
        $('#form_gg_over').submit();
    }
}


/*
                            {% ifequal order.status 'waitPay' %}
                                <a>
                                    <button  class="orderListItemConfirm" id="ope_btn" onclick="go_btn();">付款</button>
                                </a>
                            {% endifequal %}
                            {% ifequal order.status 'waitConfirm' %}
                                <a>
                                    <button  class="orderListItemConfirm" id="ope_btn" onclick="go_btn();">确认收货</button>
                                </a>
                            {% endifequal %}
                            {% if order.status == 'finish' %}
                                <a href="{% url 'OPERATION:review' %}">
                                    <button  class="orderListItemReview" disabled>交易完成</button>
                                </a>
                            {% endif %}
                            */