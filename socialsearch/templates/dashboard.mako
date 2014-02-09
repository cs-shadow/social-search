<%include file="header.mako"/>

<div class="container">
  <div class="row text-center demo-row">
    <div class="col-xs-8">      
      <div class="row text-center demo-row">
        <div class="col-xs-3">
          <!--     <div style="float: left; width: 35%;"> -->
          <img src="http://placehold.it/150x150" style="width:75px;">
        </div>
        <div class="col-xs-9" style="postion:absolute;height:75px;">    
          <!--    <div style="float: right; width: 65%;"> -->
          <p id="topic-content" style="text-align:left">
          lorem ipsem;<br />

          </p>
          <div style="position:absolute;text-align:left">
            <a href="#">Check it out</a>    
          </div>
        </div>
      </div>
      <hr />
      <div class="row text-center demo-row">
        <div class="col-xs-3">
          <!--     <div style="float: left; width: 35%;"> -->
          <img src="http://placehold.it/150x150" style="width:75px;">
        </div>
        <div class="col-xs-9" style="postion:absolute;height:75px;">    
          <!--    <div style="float: right; width: 65%;"> -->
          <p id="topic-content" style="text-align:left">
          lorem ipsem;<br />

          </p>
          <div style="text-align:left">
            <a href="#">Check it out</a>   
          </div>
          <div style="text-align:left" class="vote-post">
            <a href="post_like/1"><i class="icon-large icon-thumbs-up"></i>Upvote</a> 
            <a href="post_dislike/1"><i class="icon-large icon-thumbs-down"></i>Downvote</a>   
          </div>
        </div>
        </div>
        </div>

    <div class="col-xs-4 center">
      <div class="col-xs-12">
        <a href="javascript:addPostModal()" class="btn btn-block btn-lg btn-primary"> Add a question </a>
      </div>    
      <h3>Notifications</h3>
      <p> Test Notifications </p>
    </div>    
  </div>    
</div>    

<%include file="footer.mako"/>
