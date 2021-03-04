<template>
<div class="footer">
    <div class="about">
        <p>©2021 Zhangzyb</p>
        <p>Power by Vue ※ Django</p>
    </div>
</div>
</template>

<script>
    export default {
        name: 'Footer'        
    }
</script>

<style scoped>
.footer{
  display: flex;
  height: 30px;
  min-height: 25px;
  background: rgba(0, 0, 0, .05);
  align-items: center;
  justify-content: center;
}

.about{
    display: flex;
    justify-content: center;
    align-items: center;
}

.about p{
    margin: 0 15px;
    color: #212121a1;
    padding: 2px 0;
}
</style>