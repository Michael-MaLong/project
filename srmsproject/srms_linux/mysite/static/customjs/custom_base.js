/**
 * Created by Administrator on 2016/3/20 0020.
 */

datepickerOptions = {
    language: 'zh-CN',
    format: "yyyy-mm-dd",
    autoclose: true,
    todayHighlight: true
};

datepickerOptionsMonth = {
    language: 'zh-CN',
    format: "yyyy-mm-dd",
    startView: 2,
    maxViewMode: 1,
    minViewMode: 1,
    changeMonth: true,
    changeYear: true,
    showButtonPanel: true,
    showMonthAfterYear: true,
    todayHighlight: true,
    autoclose: true
};

function select_dept(bindId, modelId) {
    get_all_dept(bindId, false);
    $(modelId).modal({backdrop: 'static', keyboard: false})
}


function address_modal(id_string, disable_area) {
    $("#myAddressModal").modal({backdrop: 'static', keyboard: false});
    $("#city_1").citySelect({prov: "北京", nodata: "none"});
    var target = document.getElementById('change_address');
    target.onclick = function () {
        var dist = "";
        var province = $('.prov option:selected').text();
        var city = $('.city option:selected').text();
        if (disable_area) {
            dist = $('.dist option:selected').text();
        }
        var address_str = province + city + dist;
        $('#' + id_string).val(address_str);
    };
}

function custom_ajax_post_new(url, param) {
    $.ajax({
        async: false,
        url: url,
        type: 'POST',
        dataType: 'JSON',
        data: param,

        success: function (data, textStatus) {
            code = data.code;
            var msg = data.msg;
            alert(msg);

        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest);
            console.log(textStatus);
            console.log(errorThrown);
            alert("异常");
            code = 0
        }
    });
    return code
}

function custom_ajax_post(url, param) {
    var result = 0;
    $.ajax({
        async: false,
        url: url,
        type: 'POST',
        dataType: 'JSON',
        data: param,

        success: function (data, textStatus) {
            var code = data.code;
            var msg = data.msg;
            alert(msg);
            result = 1
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log(XMLHttpRequest);
            console.log(textStatus);
            console.log(errorThrown);
            alert("异常");
            result = 0
        }
    });
    return result
}

function batch_delete(url) {
    var ids = "";
    $("input[name='db_id']").each(function () {
        if ($(this).is(":checked")) {
            ids += $(this).val() + ",";
        }
    });
    ids +="-1";
    if (!ids|ids=="-1") {
        alert("至少选择一条数据")
    } else {
        var result=custom_ajax_post(url, {"ids": ids});
        if(result==1){
            window.location.reload();
        }
    }

}