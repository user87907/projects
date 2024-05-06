<?php
include("./include/header.php");

if (isset($_GET['post'])) {
    $post_id = $_GET['post'];

    $post = $db->prepare('SELECT * FROM posts WHERE id = :id');
    $post->execute(['id' => $post_id]);
    $post = $post->fetch();
}

if (isset($_POST['post_comment'])) {

    if (trim($_POST['name']) != "" || trim($_POST['comment']) != "") {

        $name = $_POST['name'];
        $comment = $_POST['comment'];

        $comment_insert = $db->prepare("INSERT INTO comments (name, comment, post_id) VALUES (:name , :comment , :post_id)");
        $comment_insert->execute(['name' => $name, 'comment' => $comment, 'post_id' => $post_id]);
        
        header("Location:single.php?post=$post_id");
        exit();
    } else {
        echo "فیلد ها نباید خالی باشند";
    }
}

?>
    <div>
        <div>

            <div>
                <div class="box">
                    <?php
                    if ($post) {
                        $category_id = $post['category_id'];

                        $query_post_category = "SELECT * FROM categories WHERE id=$category_id";

                        $post_category = $db->query($query_post_category)->fetch();

                        $post_id = $post['id'];
                        

                        $comments = $db->prepare(" SELECT * FROM comments WHERE post_id=:id AND status='1' ");
                        $comments->execute(['id' => $post_id]);

                        ?>
                        <div class="row">

                            <div>
                                <img src="./upload/posts/<?php echo $post['image'] ?>" class="img-fluid" alt="">
                            </div>

                            <div class="p-3">

                                <div class="d-flex justify-content-between">
                                    <h2 class="card-title btn btn-outline-primary"><?php echo $post['title'] ?></h2>
                                    <div class="mr-2">
                                        <span class="btn btn-outline-primary"><?php echo $post_category['title'] ?></span>
                                    </div>
                                </div>
                                <p class="card-text">
                                    <?php echo $post['body'] ?>
                                </p>

                                <p class="btn btn-outline-primary"> نویسنده : <?php echo $post['author'] ?> </p>
                            </div>

                        </div>
                        <hr>
                        <div>
                            <div>

                                <form method="post">
                                    <div class="form-group">
                                        <label for="name">نام</label>
                                        <input type="name" name="name" class="form-control">
                                    </div>

                                    <div class="form-group">
                                        <label for="comment">متن کامنت</label>
                                        <textarea name="comment" class="form-control" rows="5"></textarea>
                                    </div>

                                    <button type="submit" name="post_comment" class="btn btn-outline-primary">ارسال</button>
                                </form>
                                
                            </div>
                        </div>
                        <hr>
                        <div>

                            <p>تعداد کامنت : <?php echo $comments->rowCount() ?></p>
                            <?php
                                if ($comments->rowCount() > 0) {
                                    foreach ($comments as $comment) {
                                        ?>
                                    <div>

                                        <div class="card bg-light" >

                                            <div class="card-body">
                                                <div class="d-flex align-items-center">
                                                    <img src="./img/icons/user.png" width="70" height="70" class="rounded-circle" alt="Cinque Terre">

                                                    <div class="mr-3" >
                                                        <h5 class="card-title"> <?php echo $comment['name'] ?> </h5>
                                                    </div>
                                                </div>
                                            
                                                <p class="card-text pt-3 pr-3">
                                                    <?php echo $comment['comment'] ?>
                                                </p>
                                            </div>
                                        </div>

                                        <?php
                                    }
                                }
                
                                ?>
                    <?php
                    } else {
                        ?>
                        <div class="alert alert-danger" role="alert">
                            مقاله مورد نظر پیدا نشد!!!!!
                        </div>
                    <?php
                    }
                    ?>

                </div>

            </div>

        </div>

    </div>


<?php include_once("./include/footer.php") ?>