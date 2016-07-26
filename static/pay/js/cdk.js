$(function(){
	    var $phone = $('#ph');
	    var  $alertDiv = $('#alert_div');
	    var tel_number=/^(0|86|17951)?(13[0-9]|15[0-9]|17[0-9]|18[0-9]|14[0-9])[0-9]{8}$/;
		$phone.click(function(){
			$phone.css('border','none');
		});
		
		 $('#tiyan_img').click(function(){
			 window.location.href="http://dev.i-caiwu.com/wxpay";
			// http://dev.i-caiwu.com/wxpay
			 //$('#1_step').fadeOut();
			 //$('#2_step').fadeIn();
		 });
		 
		 
		  $('#apply_num').click(function(){
              var tel = $phone.val();
			 if(tel_number.test(tel)){
				 $.ajax({
					 type:"post",
					 url:"http://dev.i-caiwu.com:8100/coupons/",
					 data:"phone="+tel+"&sendmsg=1&properties=2",
					 error:function(data){
						 $alertDiv.text('系统异常，请稍后再试。').fadeIn(function(){
							 setTimeout(function(){
								 $alertDiv.fadeOut();
							 },4000);
						 });

					 },
					 success:function(data){
						 if(data=="已领取"){
							 $alertDiv.text('您已领取过，别太贪心哦').fadeIn(function(){
								 setTimeout(function(){
									 $alertDiv.fadeOut();
								 },4000);
							 });
						 }else {
							 $('#2_step').fadeOut();
							 $('#3_step').fadeIn();
						 }
					 }

				 });
			 }else{
				 $phone.css('border','1px solid red');
				 return ;
			 }
			 
			 
			 
		 });

	 
	});
