for cube_scale in 0.9 0.95 1.0 1.05 1.1 
do
bash scripts/gen_grasp.sh $cube_scale digit_grasp_cache num_envs=1024
done
