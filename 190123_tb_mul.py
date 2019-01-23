import tensorflow as tf
a=tf.constant(20, name='a')
b=tf.constant(30, name='b')

mul_op=a*b
sub_op=a-b
plus_op=a+b

# 세션 실행
sess = tf.Session()

# tensor board
tw=tf.summary.FileWriter('log_dir', graph=sess.graph)

# 세션 실행
print(sess.run(mul_op))
print(sess.run(sub_op))
print(sess.run(plus_op))