Issue：--name空白参数未拦截
-环境:待确认
-复现:sdt-greet --name "   "
-实际:输出Hello,  !，退出码0
-期望:拒空白输入，非0退出

校验name参数空白输入

问题:--name传全空白，程序产生无效输出。
方案:strip为空调用sys.exit(2)拦截参数。
[Blocking]
行为:未校验--name全空白输入。
风险:空白视为合法参数，输出无意义内容。
建议:name.strip()为空执行sys.exit(2)退出。
