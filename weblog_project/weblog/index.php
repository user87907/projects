<?php
include_once("./include/header.php");
include_once('./include/slider.php');

if (isset($_GET['category'])) {
  $category_id = $_GET['category'];

  $posts = $db->prepare('SELECT * FROM posts WHERE category_id = :id');
  $posts->execute(['id' => $category_id]);
 
} else {
  $query_posts = "SELECT * FROM posts ORDER BY id DESC";
  $posts = $db->query($query_posts);

}

?>

<section class="py-3">


          <?php
          
          if ($posts->rowCount() > 0) {
            foreach ($posts as $post) {

              $category_id = $post['category_id'];

              $query_post_category = "SELECT * FROM categories WHERE id=$category_id";


              $post_category = $db->query($query_post_category)->fetch();
              
              ?>
              
                    <!-- <div class="card mb-3" > -->

                <div class="card" >
                  <img src="./upload/posts/<?php echo $post['image'] ?>" class="card-img-top" alt="...">
                  <div class="card-body">
                    <div class="d-flex justify-content-between">
                      <h5 class="card-title btn btn-outline-primary"><?php echo $post['title'] ?></h5>
                      <div><span class="btn btn-outline-primary"> <?php echo $post_category['title'] ?> </span></div>
                    </div>
                    <p class="card-text text-justify">
                      <?php echo substr($post['body'], 0, 500) . "..." ?>
                    </p>
                    <div class="d-flex justify-content-between">
                      <a href="single.php?post=<?php echo $post['id'] ?>" class="btn btn-outline-primary stretched-link" style="margin-bottom: 10px;" >مشاهده</a>
                      <p class="btn btn-outline-primary"> نویسنده : <?php echo $post['author'] ?> </p>
                    </div>
                  </div>
                </div>

              </div>

            <?php
              }
            } else {
              ?>

            <div class="col">
              <div class="alert alert-danger">
                مقاله ای وجود ندارد!
              </div>
            </div>

          <?php
          }
          ?>
</section>


<?php include_once("./include/footer.php") ?>
