<!--  <script src="<?php echo base_url(); ?>JS/jquery.min.js"></script>
  <script src="<?php echo base_url(); ?>vendor/bootstrap/js/bootstrap.min.js"></script> -->
 

                         
        <h4 style="color:green;"><?php  echo $TicketId;?> Details</h4>
        <br/>
          <table  class="table table-striped table-bordered table-hover" id="dataTables-example" width=98%>
                <thead>
                <tr>
                    
                    <th>Date</th>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Category</th>
                    <th>Description</th>
                    <th>Resolution</th>
                    <th>Status</th>

                  </tr>

                </thead>

                 <tbody>
                                                        
               <?php
                $sn=1;
                
                if (!empty($ticket_detail)) {
                // output data of each row
                $i=0; foreach($ticket_detail  as $row):             
                ?>
                                    <tr class="odd gradeX">
                                       
                                        <td> <?php echo dateconverter($row->ReportedDate); ?></td>
                                       <td><?php echo $row->FirstName.'  '.$row->LastName; ?></td>
                                        <td><?php echo $row->ProductType; ?></td>
                                        <td><?php echo $row->Complaint_name; ?></td>
                                        <td class="center"><?php echo $row->ProblemDetails; ?></td>
                                        <td><?php echo $row->ResolutionDetails; ?></td>
                                        
                                        
                                        <td class="center"><?php echo $row->Status; ?></td>
                                    </tr>
                                  </tbody>
                    <?php endforeach; }?>
        </table>

     
<br/>

<div>

  <h4 style="color:red;">Tracking Details</h4>


          <table  class="table table-striped table-bordered table-hover" id="dataTables-example" width=50%>
                <thead>
                  <tr>  
                    <th>Date</th>
                    <th>Status</th>
                    <th>Responsible</th>
                  </tr>

                </thead>

                 <tbody>
                                                        
               <?php
                $sn=1;
                
                if (!empty($ticket_detail_tracking)) {
                // output data of each row
                $i=0; foreach($ticket_detail_tracking  as $row2):             
                ?>
                                    <tr class="odd gradeX">
                                        
                                        <td> <?php echo  $row2->Ticket_Tracking_DateTime; ?></td>
                                        <td class="center"><?php echo $row2->Ticket_Tracking_Status; ?></td>
                                       <td><?php echo $row2->FirstName.'  '.$row2->LastName; ?></td>   
                                    </tr>
                                  </tbody>
                    <?php endforeach; }?>
        </table>


</div>
    

 
    </div> 
                      