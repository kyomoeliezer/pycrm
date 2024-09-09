<!--  <script src="<?php echo base_url(); ?>JS/jquery.min.js"></script>
  <script src="<?php echo base_url(); ?>vendor/bootstrap/js/bootstrap.min.js"></script> -->
 

                         

          <table  class="table table-striped table-bordered table-hover" id="dataTables-example" width=98%>
                <thead>
                <tr>
                    <th>SN#</th>
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
                
                if (!empty($callertickets)) {
                // output data of each row
                $i=0; foreach($callertickets  as $row):             
                ?>
                                    <tr class="odd gradeX">
                                        <td><?php echo $sn; ?></td>
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

     

<div >
              <table  class="table table-condensedr" id="dataTables-example" width=98%>
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
                
                if (!empty($tickettracking)) {
                // output data of each row
                $i=0; foreach($tickettracking  as $row2):             
                ?>
                                    <tr class="odd gradeX">
                                        
                                        <td> <?php echo $row2->ReportedDate; ?></td>
                                        <td> <?php echo $row2->Ticket_Tracking_Status; ?></td>
                                       <td><?php echo $row2->FirstName.'  '.$row->LastName; ?></td>
                                      
                                    </tr>
                                  </tbody>
                    <?php endforeach; }?>
        </table>
</div>
    

 
    </div> 
                      