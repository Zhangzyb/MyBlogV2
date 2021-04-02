<template>
  <div class="comment-box">
    <div class="input-box">
      <input class="remind" placeholder="昵称" :key="1" v-model="username" />
      <input
        class="remind"
        placeholder="QQ邮箱"
        :key="2"
        v-model="email"
        @blur="checkEmail"
      />
    </div>
    <div class="msg" v-if="err_email">{{ err_email_msg }}</div>
    <div class="text-sub">
      <textarea v-model="text" :placeholder="reply_name"></textarea>
      <div class="submit" @click="submit">
        <div>发表</div>
        <div>评论</div>
      </div>
    </div>
  </div>
</template>

<script>
import { postComment } from "network/detail";

export default {
  data() {
    return {
      username: "",
      email: "",
      text: "",
      // err_name: false,
      err_email: false,
      // err_name_msg: "",
      err_email_msg: "",
    };
  },
  props: {
    parent_comment: null,
    default: null,
  },
  computed: {
    reply_name() {
      if (this.default) {
        return this.default;
      } else {
        return this.$store.state.reply_name;
      }
    },
  },
  methods: {
    // checkUser() {
    //   let re = /^[a-zA-Z][a-zA-Z0-9-_]{2,}$/;
    //   if (this.username.length === 0 || re.test(this.username)) {
    //     this.err_name = false;
    //   } else {
    //     this.err_name = true;
    //     this.err_name_msg =
    //       "昵称由字母、数字及下划线组成，必须以字母开头,最少三位";
    //   }
    // },
    checkEmail() {
      let re = /[1-9][0-9]{4,}@qq.com/;
      if (this.email.length === 0 || re.test(this.email)) {
        this.err_email = false;
      } else {
        this.err_email = true;
        this.err_email_msg = "请输入正确的QQ邮箱，仅支持qq号形式";
      }
    },
    submit() {
      if (!this.err_name && !this.err_email) {
        let data = {
          username: this.username,
          email: this.email,
          text: this.text,
          article: this.$route.params.id,
          parent_comment: this.parent_comment,
          reply_name: this.$store.state.reply_name,
        };

        postComment(data).then((res) => {
          if (data.parent_comment) {
            this.$bus.$emit("addSubComment", res.data);
          } else {
            this.$bus.$emit("addComment", res.data);
          }
          this.username = this.email = this.text = "";
          this.$swal.fire({
            text: "评论成功",
            icon: "success",
            showConfirmButton: false,
            timer: 1000,
          });
        });
      }
    },
  },
};
</script>

<style scoped>
.comment-box {
  width: 100%;
  margin: 1rem 0 0 0;
}

@media screen and (max-width: 600px) {
  .remind {
    width: 100%;
  }
}

@media screen and (min-width: 601px) {
  .input-box {
    display: flex;
    justify-content: space-between;
  }
  .remind {
    width: 48%;
  }
}

.remind {
  margin: 0.5rem 0 0 0;
  padding: 0.5rem 0 0.5rem 1rem;
  font-size: 0.9rem;
  border-radius: 0.5rem;
  border: 1px solid transparent;
  outline: none;
  background: rgba(0, 0, 0, 0.04);
}

.text-sub {
  display: flex;
  justify-content: space-between;
  margin: 0.6rem 0;
  height: 4.5rem;
}

textarea {
  width: 80%;
  font-size: 1.1rem;
  padding: 0.5rem 1rem;
  border: 1px solid transparent;
  border-radius: 0.6rem;
  outline: none;
  resize: none;
  background: rgba(0, 0, 0, 0.04);
  transition: all 0.3s;
}

.remind:hover,
.remind:focus,
textarea:hover,
textarea:focus {
  background: rgba(0, 0, 0, 0);
  border: 1px solid rgba(0, 0, 0, 0.15);
}

.submit {
  display: flex;
  width: 18%;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 0.5rem;
  color: #fff;
  cursor: pointer;
  background: #00a1d6;
}

.submit:hover {
  background: #00b5e5;
}

.msg {
  text-align: center;
  padding: 0.3rem 1rem;
  color: rgb(235, 49, 49);
}
</style>