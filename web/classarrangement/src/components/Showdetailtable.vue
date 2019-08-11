<template>
  <div class="container">
    <vxe-table
      :data.sync="tabledatalist"
      border
      resizable
      stripe
      style="white-space:pre;width:100%;font-weight:bold;font-size:20px;"
    >
      <vxe-table-column type="index" width="50"></vxe-table-column>
      <vxe-table-column field="monday" title="一" width="250"></vxe-table-column>
      <vxe-table-column field="tuesday" title="二" width="250"></vxe-table-column>
      <vxe-table-column field="wednesday" title="三" width="250"></vxe-table-column>
      <vxe-table-column field="thirsday" title="四" width="250"></vxe-table-column>
      <vxe-table-column field="friday" title="五" width="250"></vxe-table-column>
      <vxe-table-column field="saturday" title="六" width="250"></vxe-table-column>
      <vxe-table-column field="sunday" title="日" width="250"></vxe-table-column>
    </vxe-table>
  </div>
</template>

<script>
export default {
  name: "info",
  data() {
    return {
      classid: this.$cookie.get("showclassid"),
      tabledatalist: []
    };
  },
  created() {
    this.init();
    this.getdata();
  },
  methods: {
    init() {
      this.tabledatalist = [
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        },
        {
          monday: "",
          tuesday: "",
          wednesday: "",
          thirsday: "",
          friday: "",
          saturday: "",
          sunday: ""
        }
      ];
    },
    getdata() {
      this.axios.get("/courseplan/details/arrangement/").then(response => {
        var resp = response.data;
        if (resp["infostatus"]) {
          this.courseplanlist = resp["inforesult"];
          console.log(this.courseplanlist);
          var templist = [];
          var tempcourselist = [];
          var tempcount = 0;
          var unarranged = "";
          for (var n in this.courseplanlist) {
            if (this.courseplanlist[n]["class_id"] == this.classid) {
              if (this.courseplanlist[n]["bearranged"] == 1) {
                var tname = this.courseplanlist[n]["teacher_name"];
                var wlist = this.courseplanlist[n]["arrangement_week"];
                var slist = this.courseplanlist[n]["arrangement_section"];
                var roomlist = this.courseplanlist[n]["classnamelist"];
                console.log("wlist", wlist);
                console.log("slist", slist);
                for (var i = 0; i < wlist.length; i = i + 1) {
                  var weekname = "";
                  var wname = wlist[i];
                  if (wname == "一") {
                    weekname = "monday";
                  } else if (wname == "二") {
                    weekname = "tuesday";
                  } else if (wname == "三") {
                    weekname = "wednesday";
                  } else if (wname == "四") {
                    weekname = "thirsday";
                  } else if (wname == "五") {
                    weekname = "friday";
                  } else if (wname == "六") {
                    weekname = "saturday";
                  } else if (wname == "日") {
                    weekname = "sunday";
                  }
                  var sectionname = parseInt(slist[i]) - 1;
                  var coursename = this.courseplanlist[n]["course_name"];
                  var classroomname = roomlist[i];
                  /* if (coursename.indexOf("(") != -1) {
                    coursename = coursename.split("(")[0] + "(合)";
                  } */
                  this.tabledatalist[sectionname][weekname] =
                    tname +
                    " - - - - - - - - - - -【" +
                    classroomname +
                    "】 - - - - - - -  " +
                    coursename;
                }
              }
            }
          }
        } else {
          this.$message({
            message: resp["infomsg"]
          });
        }
      });
    }
  }
};
</script>

<style>
</style>
