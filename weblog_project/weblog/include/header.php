<?php
include_once("./include/config.php");
include_once("./include/db.php");

$query = "SELECT * FROM categories";

$categories = $db->query($query);

?>
<!DOCTYPE html>
<html lang="fa" dir="rtl">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous" />

    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" integrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous" />
    <link rel="stylesheet" href="./css/style.css" />
    <title>WEBLOG</title>
</head>

<body>

<nav class="navbar navbar-expand-lg navbar-light bg-dark" >
<button type="button" class="btn btn-outline-light" style="margin: 0px 40px;" >
  <a href="index.php">
  <i class="fas fa-home" ></i>
    صفحه اصلی
  </a>
</button>
<button type="button" class="btn btn-outline-light">
  <a target="_blank" href="admin/signin.php">
  <i class="fa fa-user" aria-hidden="true"></i>
     ورود
  </a>
</button>


  <div class="collapse navbar-collapse"  id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <button type="button" class="btn btn-outline-light">
      <li class="nav-item dropdown">
        <a class=" dropdown-toggle" href="" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        <i class="fas fa-folder-open" aria-hidden="true"></i>
             دسته بندی
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
             <?php
                    if ($categories->rowCount() > 0) {
                        foreach ($categories as $category) {
                            ?>
          <a class="dropdown-item" <?php echo ( isset($_GET['category']) && $category['id'] == $_GET['category']) ? "active" : ""; ?> href="index.php?category= <?php echo $category['id'] ?>"> <?php echo $category['title'] ?></a>
          <?php
                        }
                    }
                    ?>        
    </ul>
    </button>
    <form action="search.php" method="get" class="form-inline my-2 my-lg-3">
      <input name="search" class="form-control mr-sm-2" type="search" placeholder="دنبال چی می گردی ؟" >
      <button id="search-button" type="submit" class="btn btn-outline-light">
    <i class="fas fa-search"></i>
  </button>
    </form>
  </div>
</nav>

