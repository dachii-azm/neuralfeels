for cube_scale in 0.9 0.95 1.0 1.05 1.1 
do
bash scripts/gen_grasp.sh $cube_scale custom_grasp_cache num_envs=1
done
