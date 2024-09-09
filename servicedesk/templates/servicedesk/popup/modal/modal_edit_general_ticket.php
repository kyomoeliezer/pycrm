
<!--  <script src="<?php echo base_url(); ?>JS/jquery.min.js"></script>
  <script src="<?php echo base_url(); ?>vendor/bootstrap/js/bootstrap.min.js"></script> -->
 

<div id= '' class='bs-example'>
    <div class="col-md-12" >

            
                <div class="modal-header">
                                <div class="modal-header"">
                                 <h4 ><?php echo 'Update Ticket!'; ?> </h6>
                              </div>
                  
                              <?php foreach ($tickets_detail as $value):?>
                              
                              
                 
                                  <?php //echo form_open('Popup/general_edit_complain');?>
                                  <form id="edit_form" method="POST">
                                      <input name="callerno" type="hidden" id="callerno" value="<?php echo $value->MobileNumber; ?>" > 
                                         <input name="TicketId" type="hidden" id="TicketId" value="<?php echo $TicketId; ?>" > 

                                       <div class="form-row col-md-12">
                                        <div class="form-group col-md-6">
                                            <label>Product Type </label>
                                            <select class="form-control select2" name="producttype" required="true" id="producttype_pop" required="required">
                                            <option value="">--Select Product Type--</option>
                                        <?php // get Product types from the database
                                        foreach($producttypes as $row):

                                            echo '<option value="'.$row->ProductTypeId.'"';
                                            if ($row->ProductTypeId==$value->ProductTypeId) echo 'selected';
                                            echo '>'.$row->ProductType.'</option>'; 
                                         endforeach;
                                           ?>
                                           </select>
                                        </div>
                                         <div class="form-group col-md-6">
                                           <label>Product Category</label>
                                            
                                            <select class="form-control select2" required="true" name="comp_subproductid"
                                             id="Complaints_pop">
                                            <option value="<?php echo $value->ProductType_complaintId; ?>"><?php echo $value->Complaint_name;?></option>
                                                    
                                            </select>
                                        </div>
                                     </div>
                                    <div class="form-row col-md-12">
                                        <div class="form-group col-md-12">
                                           <label>Description</label>
   <textarea  class="form-control" required="true" id="Complaints" name="Description"><?php if (!empty($value->ProblemDetails)) echo $value->ProblemDetails;?></textarea>
                                        </div>
                                        
                                    </div>
                                     <div class="form-row col-md-12">
                                        <div class="form-group col-md-12">
                                            <label>Response</label>
        <textarea name="comp_response"  class="form-control"  id="compResp" ><?php echo $value->ResolutionDetails;?></textarea>
                                        </div>
                                    </div>
                                    <div class="form-row col-md-12">
                                        
                                    
                                        <button type="submit"  id='save' class="btn btn-success col-md-12"  style="text-align: center; width:100%;" >Save</button>

                                        
                                                      
                                                        
                                                     </div>
                                                       <?php  //echo form_close(); ?>
                                      </form>

                                        
                                     <!--   <button type="submit" class="btn btn-default">Submit Button</button>
                                        <button type="reset" class="btn btn-default">Reset Button</button>-->

                                   
                                       </div>
                                     </div>
                                   </div>
                                 <?php endforeach;?>



     

    
<script>
jQuery(document).ready(function () {
        
        /*alert('data');*/
       /* var number=$("#number").val();
        var contactid=$("#contactid").val();*/
         // code to get all records from table via select box
 $('#producttype_pop').change(function()
 { 
 /*alert('pop in');*/
  var id = $(this).find(":selected").val();



var dataString = '&type='+ id ;
    /*alert(dataString);*/
 $.ajax
  ({
   type : "POST",
   url: '<?php echo base_url(); ?>Tickets/get_product_titles',
   data: dataString,
   cache: true,
   success: function(data)
   {
    /* alert(data);*/
       
    $("#Complaints_pop").html(data);
   }
    
  });
 })
 //$('#tabs').tab();
    });

/*var form = new FormData($('#edit_form')[0]);
form.append('view_type','addtemplate');
alert('kyomo999');
$.ajax({
    type: "POST",
    url: '<?php echo site_url('Popup/general_edit_complain'); ?>',
    data: form,
    cache: false,
    contentType: false,
    processData: false,
    success:  function(data){
        //alert("---"+data);
        alert("Settings has been updated successfully.");
        window.location.reload(true);
    }
});*/
/* if {
   
    $.ajax({
    type: "POST",
    url: '<?php echo site_url('Popup/general_edit_complain'); ?>',
    data: jQuery("#edit_form").serialize(),
    cache: false,
    success:  function(data){
      alert('success! Update')
    }
  });

}*/


/*$(document).ready(function($) {*/
 $('#edit_form').submit( function (ev) {
    ev.preventDefault();  
 
  
  if($('#Complaints_pop').val() == ''){
      alert('Complaints title is required');
      ev.preventDefault();
               return false;
   }

  else if($('#Complaints').val()==' '){
      alert('Description is required!');
      ev.preventDefault();
               return false;
   }

 else {
    /* var datastring ='TicketId='+$('#TicketId').val()+'&callerno='+$('#callerno').val()+'&comp_subproductid='+$('#Complaints_pop').val()+'&comp_response='+$('#compResp').val()+'&Description='+$('#Complaints').val();
*/
      $.ajax({
      type: "POST",
      url: '<?php echo base_url(); ?>index.php/Popup/general_edit_complain',
      data:$('#edit_form').serialize(),
      
      success:  function(data){
        
        alert('success! Update');
        location.reload();
      }

    });
    return;

   }
});
/*});*/





</script>  
       

 
    </div> 
                  