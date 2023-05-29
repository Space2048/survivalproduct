<template>
    <n-space vertical align="center">
        <n-card title="Space空" size="huge">
            <n-tabs 
            class="card-tabs"
            default-value="signin"
            justify-content="center"
            size="large"
            animated
            pane-wrapper-style="margin: 0 -4px"
            pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;">
            <n-tab-pane name="signin" tab="登录">
                <n-form>
                <n-form-item-row label="用户名">
                    <n-input />
                </n-form-item-row>
                <n-form-item-row label="密码">
                    <n-input />
                </n-form-item-row>
                </n-form>
                <n-button type="primary" block secondary strong>
                登录
                </n-button>
            </n-tab-pane>
            <n-tab-pane name="signup" tab="注册">
                <n-form>
                <n-form-item-row label="用户名">
                    <n-input />
                </n-form-item-row>
                <n-form-item-row label="密码">
                    <n-input />
                </n-form-item-row>
                <n-form-item-row label="重复密码">
                    <n-input />
                </n-form-item-row>
                </n-form>
                <n-button type="primary" block secondary strong>
                注册
                </n-button>
            </n-tab-pane>
            </n-tabs>
        </n-card>
    </n-space>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useMessage } from 'naive-ui'
export default defineComponent({
  setup () {
    return {
      size: ref<'small' | 'medium' | 'large'>('medium')
    }
  }
})
</script>

<style scoped>
.n-card {
  min-width: 800px;
}
</style>