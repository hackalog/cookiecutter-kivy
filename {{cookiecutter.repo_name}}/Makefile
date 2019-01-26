.DEFAULT_GOAL := show-help
.PHONY: show-help depend create_environment requirements check_environment xcode build_done release

CONDA_ENV := {{ cookiecutter.conda_env_path }}
PROJECT_NAME := {{ cookiecutter.repo_name }}

## Remove temporary build files
clean:
	rm .ios_build_done

## Remove all build files, including caches and platform tools
reallyclean: clean
	rm -rf .buildozer


## Ensure python environment and all dependencies are set-up correctly
depend: check_environment

## Create conda environment for running this project
create_environment:
	$(CONDA_ENV) create -n $(PROJECT_NAME) -f environment.yml

## Install or update Python Dependencies
requirements: check_environment environment.lock

environment.lock: environment.yml
	$(CONDA_ENV) update -n $(PROJECT_NAME) -f $<
	$(CONDA_ENV) export -n $(PROJECT_NAME) -f $@

check_environment:
ifneq (${CONDA_DEFAULT_ENV}, $(PROJECT_NAME))
	$(error Must activate `$(PROJECT_NAME)` environment before proceeding)
endif

## Create iOS release version
ios-release: requirements
	buildozer ios release
	touch .ios_build_done

## Create iOS debug version
ios-debug: requirements
	buildozer ios debug
	touch .ios_build_done

ios-build-done: .build_done
	@echo "Must run `make ios-release` or `make debug`"

## Open xcodeCreate iOS release version
xcode: requirements
	buildozer ios xcode

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
#	* save line in hold space
#	* purge line
#	* Loop:
#		* append newline + line to hold space
#		* go to next line
#		* if line starts with doc comment, strip comment character off and loop
#	* remove target prerequisites
#	* append hold space (+ newline) to line
#	* replace newline plus comments by `---`
#	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>

show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
