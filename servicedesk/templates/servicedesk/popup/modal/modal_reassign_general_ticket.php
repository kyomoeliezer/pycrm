<!--  -->
 

<div id= '' class='bs-example'>
    <div class="col-md-12" >

            
                <div class="modal-header">
                                <div class="modal-header"">
                                 <h4 ><?php echo 'Reassign Ticket!'; ?> </h6>
                              </div>
                  
                              <?php foreach ($tickets_detail as $value):?>
                              
                              
                 
                                  <?php //echo form_open('Popup/general_attend_complain_action');?>
                                  <form id="edit_form" method="POST">
                                      <input name="callerno" type="hidden" id="number" value="<?php echo $value->MobileNumber; ?>" > 
                                         <input name="TicketId" type="hidden" id="TicketId" value="<?php echo $TicketId; ?>" > 

                                       <div class="form-row col-md-12">
                                        <div class="form-group col-md-6">
                                            <label>Product Type </label>
                                            <select class="form-control select2" name="producttype" required="true" id="producttype_pop" required="required" readonly>
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
                                            
                                            <select class="form-control select2" required="true" name="comp_subproductid" id="Complaints_pop" readonly>
                                            <option value="<?php echo $value->ProductType_complaintId; ?>"><?php echo $value->Complaint_name;?></option>
                                                    
                                            </select>
                                        </div>
                                     </div>
                                    <div class="form-row col-md-12">
                                        <div class="form-group col-md-12">
                                           <label>Description</label>
                                            
                                            <textarea  col="80"  rows="3" class="form-control" required="true" id="Complaints" name="Description">
                                              <?php echo $value->ProblemDetails;?>
                                            </textarea>
                                        </div>
                                        
                                    </div>
                                     <div class="form-row col-md-12">
                                        <!-- <div class="form-group col-md-12">
                                            <label>Response</label>
                                            <textarea name="comp_response" cols="80" rows="2" class="form-control"  id="compResp" ><?php echo $value->ResolutionDetails;?></textarea>
                                        </div> -->
                                        <input name="Status" type="hidden" id="number" value="Reassigned" >
                                        <div class="form-group col-md-12">
                                            <label>Responsible</label>
                                            <select name="assigned" class="form-control select2" id="assigned" required="true">
                                              <option value="">Select Staff</option>
                                                        <?php // get Product types from the database
                                                      foreach($staff as $strow):
                                                      if ($strow->UserId !=$UserId){
                                                          echo '<option value="'.$strow->UserId.'"';
                                                          
                                                          echo '>'.$strow->FirstName.'  '.$strow->LastName.'</option>'; 
                                                        }
                                                       endforeach;
                                                         ?>
                                                        
                                            </select>
                                        </div>
                                    </div>

                                    <div class="form-row col-md-12">
                                        
                                    
                                        <button type="submit" class="btn btn-success col-md-12" style="text-align: center; width:100%;" >Reassign</button>

                                        
                                                      
                                                        
                                                     </div>
                                                       <?php // echo form_close(); ?>
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

$('#edit_form').submit( function (ev) {
    ev.preventDefault();  
  
  if($('#Status').val() == ''){
      alert('Status is required');
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
      url: '<?php echo base_url(); ?>index.php/Popup/general_reassign_complain_action',
      data:$('#edit_form').serialize(),
      
      success:  function(data){
        
        alert('success! Reassigned');
        location.reload();
      }

    });
    return;

   }
});

</script>  
       
</div>
<style>
  input[readonly]{
  background-color:transparent;
  border: 0;
  font-size: 1em;
}
</style> 
                  