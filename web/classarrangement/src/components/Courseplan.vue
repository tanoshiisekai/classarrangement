<template>
  <div class="container">
    <Navigator defaultActive="courseplan"></Navigator>
    <div v-for="courseplan in courseplans" :key="courseplan.courseplan_id">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>班级名称</span>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import Navigator from "@/components/Navigator";
export default {
  name: "courseplan",
  components: {
    Navigator
  }
};
</script>

<style>
</style>
