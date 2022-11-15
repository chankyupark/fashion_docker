cp -rf ../aai4r_edge_interfaces .
docker build --rm -t aai4r/fashion2 -f fashion2_aai4r.Dockerfile .
rm -rf aai4r_edge_interfaces
docker tag aai4r/fashion2 robot-registry.ainize.ai/aai4r/fashion2
