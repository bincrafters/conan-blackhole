#include <blackhole/logger.hpp>
#include <blackhole/root.hpp>

int main(int argc, char** argv)
{
	auto log = blackhole::builder<blackhole::root_logger_t>();
	return 0;
}
